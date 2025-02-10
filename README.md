# Audio-to-Text-Transcriber 🎙️
A Multilingual Audio Transcriber that converts speech into text using OpenAI's Whisper, Streamlit, and FFmpeg. This tool allows users to upload audio files and get highly accurate transcriptions in multiple languages.

# 🚀 Features
 🎧 Supports multiple audio formats (MP3, WAV, M4A, FLAC) 
 🌍 Multilingual transcription (English, French, Spanish, German, Chinese, Arabic, Hindi, Urdu)
 🖥️ User-friendly Streamlit interface
 ⚡ Fast and efficient transcription powered by OpenAI's Whisper
 🔊 Audio playback support
 📌 Installation & Setup
# 1️⃣ Clone the Repository

bash

# git clone https://github.com/your-username/Audio-to-Text-Transcriber.git

# 2️⃣ Install Dependencies

 pip install -r requirements.txt
# 3️⃣ Install FFmpeg
Download and install FFmpeg from:
# 🔗 https://ffmpeg.org/download.html

Then, update the FFmpeg path in the script:

# Python

 ffmpeg_path = r"C:\Path\To\Your\FFmpeg\bin\ffmpeg.exe"
 os.environ["PATH"] += os.pathsep + os.path.dirname(ffmpeg_path)
# 4️⃣ Run the Application

 streamlit run app.py
 
# 🎯 How to Use
 1️⃣ Upload an audio file (MP3, WAV, M4A, FLAC).
 2️⃣ Select the transcription language from the dropdown.
 3️⃣ Click the "Transcribe" button to start processing.
 4️⃣ View and copy the transcribed text.

# 🛠️ Technologies Used
 Python
 OpenAI Whisper (Speech Recognition)
 Streamlit (Frontend UI)
 FFmpeg (Audio processing)
# 📌 To-Do & Future Improvements
 Add real-time speech-to-text transcription
 Improve UI with enhanced styling
 Allow users to export transcriptions as text files
 Integrate punctuation and grammar improvements
# 📜 License
This project is open-source and licensed under the MIT License.

# 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

# 🔗 Connect With Me
# 📧 Email: ownshah962@gmail.com
# 🌐 GitHub: https://github.com/MAhmed9211/

