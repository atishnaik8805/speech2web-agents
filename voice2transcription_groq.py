import sounddevice as sd
import numpy as np
import os
from dotenv import load_dotenv
from groq import Groq
import soundfile as sf

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

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

def save_audio_to_file(audio, filename="recorded_audio.wav", fs=16000):
    sf.write(filename, audio, fs)
    return filename

def transcribe_audio(filename):
    print("Transcribing...")
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
        print(transcription.text)
        return transcription.text

def voice2transcriptionmain():
    audio = record_audio()
    print(f"Audio shape: {audio.shape}, dtype: {audio.dtype}")  # Debugging print to check the audio data
    audio_file = save_audio_to_file(audio)
    transcription = transcribe_audio(audio_file)
    print("Transcription:", transcription)
    return transcription

if __name__ == "__main__":
    voice2transcriptionmain()

      