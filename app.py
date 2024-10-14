from voice2transcription_groq import voice2transcriptionmain
from transctiption2JSON import transcription2JSONmain


def main():
    trascription = trascription = voice2transcriptionmain()
    transcription2JSONmain(trascription)

if __name__ == "__main__":
    main()