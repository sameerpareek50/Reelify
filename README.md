# Reelify 🎬✨

Reelify is a web-based application that allows users to create AI-powered video reels by uploading images and/or providing text for voiceover. The app leverages advanced AI (via ElevenLabs) for text-to-speech and automates the process of generating engaging video reels, making content creation easy for everyone.

---

## 🚀 Features

- **Upload Images:** Add one or more images to create a visual story.
- **AI Voiceover:** Enter text to generate a realistic AI voiceover using ElevenLabs API.
- **Automatic Reel Generation:** Once you submit, the backend automatically processes your input and generates a video reel.
- **Gallery:** Browse all generated reels in a dedicated gallery.
- **Error Handling:** User-friendly error messages if no image or text is provided.
- **Modern UI:** Clean, responsive interface built with HTML, CSS, and Flask templating.

---

## 🛠️ Tech Stack & Libraries

- **Python 3.10+**
- **Flask:** Web framework for backend and routing.
- **Werkzeug:** Secure file uploads.
- **ElevenLabs:** AI text-to-speech (TTS) API.
- **uuid:** For generating unique session/folder IDs.
- **os, subprocess:** File and process management.
- **ffmpeg:** Powerful multimedia framework for combining images and audio into video reels.
- **HTML/CSS/JS:** Frontend (with Dropzone.js for drag-and-drop file uploads, if enabled).
- **Jinja2:** Flask templating engine.

### Python Libraries Used

- `flask`
- `werkzeug`
- `uuid`
- `os`
- `subprocess`
- `elevenlabs` (official Python SDK)
- `config` (for API keys and configuration)

### Flask Extensions

- **Flask Flash:** For user notifications and error messages.

### External Tools

- **FFmpeg:**  
  FFmpeg is used to process and combine the uploaded images and generated audio into a final video reel. It reads the list of images and the audio file, then creates a video with synchronized visuals and voiceover.  
  **Usage:**  
  - Converts a sequence of images into a video.
  - Merges the generated audio (from ElevenLabs) with the video.
  - Ensures the output is compatible for web playback.
  - FFmpeg is called via Python's `subprocess` module in the `generate_process.py` script.

---

## 📁 Project Structure

```
Reelify/
│
├── main.py                # Main Flask app, handles routing and logic
├── generate_process.py    # Script to generate reels from uploaded data (uses ffmpeg)
├── text_to_audio.py       # Handles text-to-speech using ElevenLabs
├── config.py              # Stores API keys and configuration
│
├── templates/
│   ├── base.html
│   ├── create.html
│   ├── gallery.html
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── create.css
│   └── reels/             # Output directory for generated reels
│
└── user_uploads/          # Temporary storage for user uploads
```

---

## ⚙️ How It Works

1. **User uploads images and/or enters text** on the `/create` page.
2. **Validation:** At least one image or text is required. If not, an error is shown.
3. **Data is saved** in a unique folder under `user_uploads/`.
4. **Automatic Processing:** The backend triggers `generate_process.py` to create a reel using the uploaded images and generated audio.
5. **FFmpeg combines** the images and audio into a video reel.
6. **Reel is saved** in `static/reels/` and shown in the `/gallery` page.

---

## 🧩 Setup & Installation

1. **Clone the repo:**
    ```bash
    git clone https://github.com/sameerpareek50/reelify.git
    cd reelify
    ```

2. **Install dependencies:**
    ```bash
    pip install flask werkzeug elevenlabs
    ```

3. **Install FFmpeg:**  
   FFmpeg must be installed and accessible in your system's PATH.
    - [Download FFmpeg](https://ffmpeg.org/download.html) and follow installation instructions for your OS.
    - To verify installation, run:
      ```bash
      ffmpeg -version
      ```

4. **Set your ElevenLabs API key:**
    - Edit `config.py` and add your API key.

5. **Run the app:**
    ```bash
    python main.py
    ```

6. **Open your browser:**  
   Go to [http://localhost:5000](http://localhost:5000)

---

<!-- ## 🖼️ Screenshots

> _Attach screenshots of your home page, create page, and gallery here to showcase the UI and workflow._

--- -->

## 📝 Challenges Faced

- **Automating Reel Generation:** Ensuring the reel is generated immediately after form submission required careful orchestration between Flask and the subprocess running the generator script.
- **Validation:** Handling cases where users submit the form without images or text, and providing clear feedback.
- **File Management:** Managing unique folders for each session and cleaning up temporary files.
- **API Integration:** Integrating with ElevenLabs for high-quality, low-latency voice synthesis.
- **FFmpeg Integration:** Ensuring FFmpeg is correctly installed and invoked from Python, and handling cross-platform compatibility.

---

## 📚 Usage Notes

- **API Key:** You must have a valid ElevenLabs API key for text-to-speech.
- **File Types:** Only `.png`, `.jpg`, and `.jpeg` images are supported.
- **FFmpeg:** FFmpeg must be installed and available in your system's PATH for video generation to work.
- **Reel Output:** Generated reels are stored in `static/reels/` and can be accessed via the gallery.

---

<!-- ## 🌟 Demo

> _Add a link to a live demo if available, or a short GIF/video of the workflow._

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

--- -->

## 🔗 Project Links

[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?logo=github&style=for-the-badge&logoColor=white)](https://github.com/sameerpareek50/reelify)
&nbsp;
[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=render&logoColor=white)](https://reelify-cgnr.onrender.com)

---

**Showcase your creativity and AI-powered video editing skills with Reelify!**