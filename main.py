import os
import whisper
import streamlit as st
from tempfile import NamedTemporaryFile

# Load the Whisper model (Force CPU mode for better compatibility)
model = whisper.load_model("base", device="cpu")

# Streamlit UI
st.title("Multilingual Audio Transcriber with Whisper")

# File uploader
uploaded_file = st.file_uploader("Upload an Audio File", type=["mp3", "wav", "m4a", "flac"])

# Language selection dropdown
languages = {
    "English": "en", "French": "fr", "Spanish": "es",
    "German": "de", "Chinese": "zh", "Arabic": "ar",
    "Hindi": "hi", "Urdu": "ur"
}
selected_language = st.selectbox("Select Language for Transcription", list(languages.keys()))

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio/mp3")

    if st.button("Transcribe"):
        try:
            # Save the uploaded file as a temporary file
            with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
                temp_audio.write(uploaded_file.read())
                temp_audio_path = temp_audio.name  # Get the temp file path

            # Transcribe the audio
            result = model.transcribe(temp_audio_path, language=languages[selected_language])

            # Display the transcribed text
            st.subheader("Transcribed Text:")
            st.write(result["text"])

        except Exception as e:
            st.error(f"An error occurred: {e}")
