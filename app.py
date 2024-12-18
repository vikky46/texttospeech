import streamlit as st
from gtts import gTTS
from io import BytesIO
import base64

def text_to_speech(text):
    tts = gTTS(text)
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp

def main():
    page = st.sidebar.selectbox("Choose a page", ["Project Description", "Text to Speech"])
    
    if page == "Project Description":
        project_description()
    elif page == "Text to Speech":
        text_to_speech_page()

def project_description():
    st.title("Project Description")
    st.write("""
    ## Text to Speech Web Application
    
    This project is a simple web application built using Streamlit and Google Text-to-Speech (gTTS) library. 
    It allows users to convert text input into speech output. The application consists of two main pages:
    
    1. **Project Description Page**: This page provides an overview of the project and its purpose.
    2. **Text to Speech Page**: This page enables users to input text and convert it into speech.
    
    ### How to Run the App:
    
    1. Install the required packages using `pip install -r requirements.txt`.
    2. Run the Streamlit app using `streamlit run app.py`.
    
    ### Libraries Used:
    
    - Streamlit: A framework for building web applications with Python.
    - gTTS (Google Text-to-Speech): A Python library and CLI tool to interface with Google Translate's text-to-speech API.
    """)

def text_to_speech_page():
    st.title("Text to Speech")

    # Text input
    text_input = st.text_area("Enter text:", "Hello, World!")

    # Convert text to speech
    if st.button("Convert to Speech", key="convert_button", help="Click to convert text to speech"):
        audio_data = text_to_speech(text_input)
        st.audio(audio_data.getvalue(), format='audio/mp3')

        # Download button for the audio file
        download_link = generate_download_link(audio_data, "text_to_speech.mp3", "Download Audio")
        st.markdown(download_link, unsafe_allow_html=True)

def generate_download_link(audio_data, file_name, link_text):
    """Generate a download link for the given audio data."""
    with BytesIO() as buffer:
        buffer.write(audio_data.getvalue())
        b64 = base64.b64encode(buffer.getvalue()).decode()
        href = f'<a href="data:application/octet-stream;base64,{b64}" download="{file_name}">{link_text}</a>'
    return href

if __name__ == "__main__":
    main()
