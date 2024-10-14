# import whisper
# import sounddevice as sd
# import numpy as np

# # Load the model
# model = whisper.load_model("small")  # You can choose "small", "medium", or "large" based on your needs

# def record_audio(duration=5, fs=16000):
#     print("Recording...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)  # Single channel
#     sd.wait()  # Wait until recording is finished
#     print("Recording complete.")
#     return audio

# def transcribe_audio(audio):
#     # Convert audio to the format required by Whisper
#     audio_input = whisper.pad_or_trim(audio)
#     # Make a prediction
#     result = model.transcribe(audio_input)
#     return result['text']

# def main():
#     duration = 5  # Record for 5 seconds
#     audio = record_audio(duration)
#     print(audio)  # Debugging print to check the audio data
#     transcription = transcribe_audio(audio)
#     print("Transcription:", transcription)

# if __name__ == "__main__":
#     main()

# import whisper
# import sounddevice as sd
# import numpy as np
# import torch

# # Load the model
# model = whisper.load_model("small")

# def record_audio(duration=5, fs=16000):  # Use 16000 Hz
#     print("Recording...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
#     sd.wait()  # Wait until recording is finished
#     print("Recording complete.")
#     return np.squeeze(audio)  # Ensure the audio array is flattened

# def transcribe_audio(audio):
#     audio_tensor = torch.tensor(audio, dtype=torch.float32)
#     audio = whisper.pad_or_trim(audio_tensor)
#     mel = whisper.log_mel_spectrogram(audio).to(model.device)
#     options = whisper.DecodingOptions()
#     result = whisper.decode(model, mel, options)
#     return result.text

# def main():
#     duration = 5  # Record for 5 seconds
#     audio = record_audio(duration)
#     print(f"Audio shape: {audio.shape}, dtype: {audio.dtype}")  # Debugging print to check the audio data
#     transcription = transcribe_audio(audio)
#     print("Transcription:", transcription)

# if __name__ == "__main__":
#     main()


## Install pip install git+https://github.com/openai/whisper.git 

import whisper
import sounddevice as sd
import numpy as np
import torch

# Load the model
model = whisper.load_model("small")

def record_audio(fs=16000, chunk_duration=0.1, silence_threshold=0.01, silence_duration=5):
    print("Recording...")
    
    chunk_size = int(chunk_duration * fs)
    silence_chunks = int(silence_duration / chunk_duration)
    audio_chunks = []
    silence_counter = 0

    def callback(indata, frames, time, status):
        nonlocal silence_counter
        volume_norm = np.linalg.norm(indata) / np.sqrt(len(indata))
        audio_chunks.append(indata.copy())
        if volume_norm < silence_threshold:
            silence_counter += 1
        else:
            silence_counter = 0

    with sd.InputStream(samplerate=fs, channels=1, dtype='float32', callback=callback):
        while silence_counter < silence_chunks:
            sd.sleep(int(chunk_duration * 1000))
    
    print("Recording complete.")
    audio = np.concatenate(audio_chunks)
    return audio.flatten()

def transcribe_audio(audio):
    print("Transcribing...")
    audio_tensor = torch.tensor(audio, dtype=torch.float32)
    audio = whisper.pad_or_trim(audio_tensor)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    print("Transcription result:", result)
    return result.text

def main():
    audio = record_audio()
    print(f"Audio shape: {audio.shape}, dtype: {audio.dtype}")  # Debugging print to check the audio data
    transcription = transcribe_audio(audio)
    print("Transcription:", transcription)

if __name__ == "__main__":
    main()

