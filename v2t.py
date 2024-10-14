import os
from dotenv import load_dotenv
from groq import Groq
import soundfile as sf

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def transcribe_audio(filename):
    print(filename)
    print("Transcribing...")
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )
        print(transcription.text)
        return transcription.text

def voice2transcriptionmain(filepath):
    transcription = transcribe_audio(filepath)
    print("Transcription:", transcription)
    return transcription
