# import streamlit as st
# from audiorecorder import audiorecorder
# import time
# import threading
# from v2t import voice2transcriptionmain

# # Title for the audio recorder section
# st.title("Audio Recorder")

# # CSS for the pulsing animation
# st.markdown("""
#     <style>
#     .pulsing {
#         display: inline-block;
#         font-size: 24px;
#         font-weight: bold;
#         color: #f00;
#         animation: pulse 1s infinite;
#     }

#     @keyframes pulse {
#         0% { opacity: 1; }
#         50% { opacity: 0.5; }
#         100% { opacity: 1; }
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Record audio
# audio = audiorecorder("Start Rec", "Stop Rec")

# # Check if audio was recorded
# if len(audio) > 0:
#     # Play the audio in the frontend
#     st.audio(audio.export().read())

#     # Save the audio to a file
#     audio.export("audio.wav", format="wav")

#     # Display audio properties
#     st.write(f"Frame rate: {audio.frame_rate}, Frame width: {audio.frame_width}, Duration: {audio.duration_seconds} seconds")

#     # Create a placeholder for the "Transcribing..." animation
#     placeholder = st.empty()

#     # Variable to control the animation loop
#     transcribing = True

#     def animate_transcribing():
#         while transcribing:
#             placeholder.markdown("<div class='pulsing'>Transcribing...</div>", unsafe_allow_html=True)
#             time.sleep(0.5)

#     # Start the animation in a separate thread
#     animation_thread = threading.Thread(target=animate_transcribing)
#     animation_thread.start()

#     # Perform the transcription
#     transcription = voice2transcriptionmain('audio.wav')

#     # Stop the animation
#     transcribing = False

#     # Wait for the animation thread to finish
#     animation_thread.join()

#     # Display the transcription results
#     placeholder.empty()  # Clear the placeholder
#     st.write(transcription)


# import streamlit as st

# # Set the page configuration
# st.set_page_config(page_title="Radial Gradient Background", layout="centered")

# # Custom CSS for the radial gradient background and centered cards with icons
# page_bg_img = '''
# <style>
# body {
#     background: radial-gradient(circle, #ffcccc, #6666ff);
#     height: 100vh;
#     margin: 0;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }
# .center-content {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     flex-direction: column;
# }
# .stButton > button {
#     display: none;
# }
# .card {
#     width: 200px;
#     height: 150px;
#     background: white;
#     border-radius: 10px;
#     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     margin: 20px;
#     text-align: center;
#     padding-top: 20px;
#     font-size: 20px;
#     cursor: pointer;
#     transition: transform 0.3s, box-shadow 0.3s;
# }
# .card:hover {
#     transform: scale(1.05);
#     box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
# }
# .card i {
#     font-size: 50px;
#     margin-bottom: 10px;
#     display: block;
# }
# i {
#     color: black; /* Change text color to black */
# }
# i div {
#     color: black; /* Change font icon color to black */
# }

# </style>
# '''

# # Apply the CSS
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Load Font Awesome
# st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)

# # Main page content
# st.markdown("<div class='center-content'>", unsafe_allow_html=True)

# # Create two hidden buttons
# if st.button("Hidden Card 1", key="card1"):
#     st.write("Card 1 clicked!")
# if st.button("Hidden Card 2", key="card2"):
#     st.write("Card 2 clicked!")

# # Create the visible cards
# st.markdown("""
#     <div class='center-content'>
#         <div class='card' onclick="document.querySelector('button[data-key=card1]').click()">
#             <i class="fas fa-hard-hat"></i>
#             <div>Construction Worker</div>
#         </div>
#         <div class='card' onclick="document.querySelector('button[data-key=card2]').click()">
#             <i class="fas fa-user-friends"></i>
#             <div>Event Attendee</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("</div>", unsafe_allow_html=True)

# # Custom CSS for the radial gradient background and centered cards with icons
# page_bg_img = '''
# <style>
# body {
#     background: radial-gradient(circle, #ffcccc, #6666ff);
#     height: 100vh;
#     margin: 0;
#     display: flex;
#     justify-content: center;
#     align-items: center;
# }
# .center-content {
#     display: flex;
#     justify-content: center;
#     align-items: center;
#     flex-direction: row;
# }
# .stButton > button {
#     display: none;
# }
# .card {
#     width: 200px;
#     height: 150px;
#     background: white;
#     border-radius: 10px;
#     box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#     margin: 20px;
#     text-align: center;
#     padding-top: 20px;
#     font-size: 20px;
#     cursor: pointer;
#     transition: transform 0.3s, box-shadow 0.3s;
# }
# .card:hover {
#     transform: scale(1.05);
#     box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
# }
# .card i {
#     font-size: 50px;
#     margin-bottom: 10px;
#     display: block;
#     color: black;
# }
# @keyframes fadeIn {
#     from {opacity: 0;}
#     to {opacity: 1;}
# }
# .fade-in {
#     animation: fadeIn 1s;
# }
# </style>
# '''

# # Apply the CSS
# st.markdown(page_bg_img, unsafe_allow_html=True)

# # Load Font Awesome
# st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)

# # JavaScript for page transitions
# st.markdown("""
# <script>
# function navigateTo(url) {
#     document.body.classList.add('fade-in');
#     setTimeout(() => {
#         window.location.search = url;
#     }, 1000); // Adjust the timeout to match the animation duration
# }
# </script>
# """, unsafe_allow_html=True)

# # Main page content
# st.markdown("<div class='center-content'>", unsafe_allow_html=True)

# # Create the visible cards
# st.markdown("""
#     <div class='center-content'>
#         <div class='card' onclick="navigateTo('?page=page1')">
#             <i class="fas fa-hard-hat"></i>
#             <div>Construction Worker</div>
#         </div>
#         <div class='card' onclick="navigateTo('?page=page2')">
#             <i class="fas fa-user-friends"></i>
#             <div>Event Attendee</div>
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# # Page routing
# query_params = st.query_params
# page = query_params.get('page', [''])[0]
# if page == 'page1':
#     st.write("Welcome to Page 1")
# elif page == 'page2':
#     st.write("Welcome to Page 2")

# st.markdown("</div>", unsafe_allow_html=True)

import streamlit as st


# # Configure pages
# show_pages(
#     [
#         Page("events.py", "Plans"),
#         Page("jobs.py", "Jobs"),
#     ]
# )
# Custom CSS for a larger hero component with a background for the text
hero_css = '''
<style>
.hero {
    font-size: 25px; /* Increase the font size */
    line-height: 1.5;
    font-weight: bold;
    text-align: center;
    margin-top: 50px;
    padding: 20px;
    color: transparent; /* Make the text transparent */
    background: radial-gradient(circle, #ffcccc, #6666ff);
    -webkit-background-clip: text; /* Apply the background gradient to the text */
    background-clip: text; /* Standard background clip */
    border-radius: 10px;
}
.card {
    width: 200px;
    height: 150px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin: 20px;
    text-align: center;
    padding-top: 20px;
    font-size: 20px;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}
.card i {
    font-size: 50px;
    margin-bottom: 10px;
    display: block;
    color: black;
}
</style>
'''

card_css = ''' <style>
.card {
    width: 200px;
    height: 150px;
    background: white;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin: 20px;
    text-align: center;
    padding-top: 20px;
    font-size: 20px;
    cursor: pointer;
    transition: transform 0.3s, box-shadow 0.3s;
}
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
}
.card i {
    font-size: 50px;
    margin-bottom: 10px;
    display: block;
    color: black;
}
</style>'''


# Apply the CSS
st.markdown(hero_css, unsafe_allow_html=True)

st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)
# Create the hero component
st.markdown("""
<div class="hero">
    Welcome to our innovative app! This tool listens to your speech, accurately transcribes it, and converts it into a sleek JSON format. <br><br>
    But that’s not all! This JSON data is then efficiently sent to a database in real-time. Whether you need to keep a record of important spoken information or streamline your workflow, this app has got you covered.<br><br>
    Dive in and experience the future of speech transcription!
    <br/>
    Currently we have just 2 schemas that we support.
</div>
""", unsafe_allow_html=True)

# Section for choosing between Speech to JSON conversions
# st.markdown("""
# <div class="buttons">
#     <h4>Choose Your Path</h4>
#     <div class='center-content' style="display: flex;">
#         <div class='card' onclick="()=>window.location.href='/Events'">
#             <i class="">👷</i>
#             <div>Construction Worker</div>
#         </div>
#         <div class='card' onclick="() => window.location.href='/Jobs'">
#             <i class="">📆</i>
#             <div>Event Attendee</div>
#         </div>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# Section for choosing between Speech to JSON conversions
st.markdown("<div class='buttons'><h4>Choose Your Path</h4></div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("Construction Worker"):
        st.session_state.page = '\Events'
        st.experimental_set_query_params(page='Events')
with col2:
    if st.button("Event Attendee"):
        st.session_state.page = '\Jobs'
        st.experimental_set_query_params(page='Jobs')

