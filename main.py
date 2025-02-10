import os
import whisper
import streamlit as st
from io import BytesIO

# Set the full path to the ffmpeg executable
ffmpeg_path = r"C:\Users\Del\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-7.1-full_build\bin\ffmpeg.exe"

# Add the ffmpeg directory to the system path within the Python script
os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)

# Load the Whisper model
model = whisper.load_model("base")

# Streamlit UI
st.title("Multilingual Audio Transcriber with Whisper")

# Add a file uploader for audio files
uploaded_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "m4a", "flac"])

# Language selection dropdown
languages = {"English": "en", "French": "fr", "Spanish": "es", "German": "de", "Chinese": "zh", "Arabic": "ar", "Hindi": "hi", "Urdu": "ur"}
selected_language = st.selectbox("Select Language for Transcription", list(languages.keys()))

# Add a button for transcribing the audio
if uploaded_file is not None:
    # Display the audio file on the frontend (so users can play it)
    st.audio(uploaded_file, format="audio/mp3")

    if st.button("Transcribe"):
        # Read the uploaded file and save it temporarily
        audio = uploaded_file.getvalue()
        audio_file = BytesIO(audio)
        
        # Transcribe the audio using Whisper in the selected language
        result = model.transcribe("audio.mp3", language=languages[selected_language])
        
        # Display the transcribed text
        st.subheader("Transcribed Text:")
        st.write(result["text"])
