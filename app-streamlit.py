from st_audiorec import st_audiorec
import streamlit as st
import os
import datetime
from v2t import voice2transcriptionmain
from transctiption2JSON import transcription2JSONmain


def main(file_name, schema):
    transcript = voice2transcriptionmain(file_name)
    json_data = transcription2JSONmain(transcript, schema)
    return json_data

# Create recordings directory if it doesn't exist
if not os.path.exists('recordings'):
    os.makedirs('recordings')

# Display the mic button for recording audio
st.subheader("Click the button to start and stop recording")


# Record audio using the st_audiorec() component
wav_audio_data = st_audiorec()


# Check if audio recording has completed (i.e., the Stop button has been pressed)
if wav_audio_data is not None:
    # Play the recorded audio in Streamlit
    st.audio(wav_audio_data, format='audio/wav')

    file_name = f"recordings/sample_audio.wav"

    # # Save the audio data to a file
    with open(file_name, 'wb') as f:
        f.write(wav_audio_data)

    # Display a success message with the saved file name
    st.success(f"Audio saved successfully as {file_name}")
    
    if st.button("Events"):
        st.write(main(file_name=file_name, schema='sample_schema_01'))

    if st.button('jobs'):
        st.write(main(file_name=file_name, schema='task_schema_01'))
