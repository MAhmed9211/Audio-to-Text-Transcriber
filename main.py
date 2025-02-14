import os
import whisper
import streamlit as st
from io import BytesIO
import subprocess

# Check if ffmpeg is installed
ffmpeg_installed = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
if ffmpeg_installed.returncode != 0:
    st.error("FFmpeg is not installed! Add `ffmpeg` to `packages.txt` and redeploy.")

# Load Whisper model
model = whisper.load_model("base")

# Streamlit UI
st.title("Multilingual Audio Transcriber with Whisper")

# File uploader
uploaded_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "m4a", "flac"])

# Language selection
languages = {"English": "en", "French": "fr", "Spanish": "es", "German": "de", "Chinese": "zh", "Arabic": "ar", "Hindi": "hi", "Urdu": "ur"}
selected_language = st.selectbox("Select Language for Transcription", list(languages.keys()))

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")

    if st.button("Transcribe"):
        # Read uploaded file and save it
        audio_bytes = uploaded_file.read()
        with open("temp_audio.mp3", "wb") as f:
            f.write(audio_bytes)

        # Transcribe using Whisper
        result = model.transcribe("temp_audio.mp3", language=languages[selected_language])

        # Display the transcription
        st.subheader("Transcribed Text:")
        st.write(result["text"])
