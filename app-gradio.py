import gradio as gr
from v2t import voice2transcriptionmain
from transctiption2JSON import transcription2JSONmain 

def process(filepath):
    transcription = voice2transcriptionmain(filepath)
    return transcription2JSONmain(transcription)

def main():
    demo = gr.Interface(
        fn=process,
        inputs=gr.Audio(type="filepath"),
        outputs="text"
    )
    demo.launch()

if __name__ == "__main__":
    main()
