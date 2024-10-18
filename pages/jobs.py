import streamlit as st
# from audiorecorder import audiorecorder
from st_audiorec import st_audiorec
import time
from v2t import voice2transcriptionmain
from transctiption2JSON import transcription2JSONmain
from src.db.mongoDB import insert_person_event, insert_jobs
from src.helper.validation import validateJobSchema, validaEventSchema

# Title for the audio recorder section
st.title("Audio Recorder")

# CSS for the pulsing animation
st.markdown("""
    <style>
    .pulsing {
        display: inline-block;
        font-size: 40px;
        font-weight: bold;
        color: white;
        animation: pulse 1s infinite;
    }

    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# Record audio
# audio = audiorecorder("Start Rec", "Stop Rec")
audio = st_audiorec()

# Check if audio was recorded
# if len(audio) > 0:
#     # Play the audio in the frontend
#     st.audio(audio.export().read())
if audio is not None:
    st.audio(audio, format='audio/wav')

    # Save the audio to a file
    #audio.export("audio.wav", format="wav")

    # Display audio properties
    #st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")
        # Define a filename (you can change this dynamically as per your needs)
    filename = "audio.wav"

    # Save the audio file
    with open(filename, "wb") as f:
        f.write(audio)

    st.success(f"Audio has been saved as {filename}")

    # Create placeholders for the animations
    placeholder_transcribe = st.empty()
    placeholder_json = st.empty()
    placeholder_processing = st.empty()
    placeholder_dbquery = st.empty()

    # Function to simulate "Transcribing..." animation and force the UI to update during transcription
    def animate_and_transcribe():
        transcription = None

        # Start "Transcribing..." animation
        for _ in range(10):
            placeholder_transcribe.markdown("<div class='pulsing'>Transcribing...</div>", unsafe_allow_html=True)
            time.sleep(0.5)
            placeholder_transcribe.markdown("<div class='pulsing' style='visibility:hidden'>Transcribing...</div>", unsafe_allow_html=True)
            time.sleep(0.5)
        
        # Perform the transcription after animation
        try:
            transcription = voice2transcriptionmain('audio.wav')  # Transcribe the recorded audio
        except Exception as e:
            transcription = f"Error occurred during transcription: {e}"

        return transcription

    # Function to simulate "JSON Conversion..." animation and perform JSON conversion
    def animate_and_convert_to_json(transcription):
        json_result = None

        # Start "Converting to JSON..." animation
        for _ in range(10):
            placeholder_json.markdown("<div class='pulsing'>Converting to JSON...</div>", unsafe_allow_html=True)
            time.sleep(0.5)
            placeholder_json.markdown("<div class='pulsing' style='visibility:hidden'>Converting to JSON...</div>", unsafe_allow_html=True)
            time.sleep(0.5)

        # Perform the JSON conversion
        try:
            json_result = transcription2JSONmain(transcription, 'jobs')  # Convert the transcription to JSON
        except Exception as e:
            json_result = f"Error occurred during JSON conversion: {e}"

        return json_result

    # Function to simulate "Processing..." animation
    def animate_processing():
        # Start "Processing..." animation
        for _ in range(10):
            placeholder_processing.markdown("<div class='pulsing'>Processing...</div>", unsafe_allow_html=True)
            time.sleep(0.5)
            placeholder_processing.markdown("<div class='pulsing' style='visibility:hidden'>Processing...</div>", unsafe_allow_html=True)
            time.sleep(0.5)

    
    def animate_and_saveindb(jsondata):
        db_result = None



        # Start "Converting to JSON..." animation
        for _ in range(10):
            placeholder_json.markdown("<div class='pulsing'>Sending the data...</div>", unsafe_allow_html=True)
            time.sleep(0.5)
            placeholder_json.markdown("<div class='pulsing' style='visibility:hidden'>Sending the data...</div>", unsafe_allow_html=True)
            time.sleep(0.5)
        try:
            db_result  = insert_jobs(jsondata)
        except Exception as e:
            db_result = f"Error occurred during JSON conversion: {e}"
        return db_result
    
    # Run the transcription animation and process the transcription
    transcription = animate_and_transcribe()

    animate_processing()

    # Clear the placeholder for the transcribing animation
    placeholder_transcribe.empty()

    # Display the transcription results in a non-editable text box with a label
    st.text_area("Transcription", value=transcription, height=150, max_chars=None, disabled=True)

    # Run the JSON conversion animation and process the transcription to JSON
    json_conversion_result = animate_and_convert_to_json(transcription)

    # Clear the placeholder for the JSON conversion animation
    placeholder_json.empty()

    # Run the processing animation
    animate_processing()

    # Clear the placeholder for the processing animation
    placeholder_processing.empty()

    # Display the JSON conversion results in a non-editable text box with a label
    st.text_area("JSON Conversion Result", value=json_conversion_result, height=150, max_chars=None, disabled=True)

    db_result = animate_and_saveindb(json_conversion_result)
    #is_valid, message = (validaEventSchema(json_conversion_result))
    print(db_result, db_result.acknowledged)

    if db_result.acknowledged:
        #db_result = animate_and_saveindb(json_conversion_result)
        st.success(f"Succesfully Saved the data")
    else:
        st.error(f"Error: {message} Please try again, with the process")


    







