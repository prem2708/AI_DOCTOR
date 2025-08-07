# 🤖 AI_DOCTOR: Vision & Voice Medical Assistant

AI_DOCTOR is an intelligent, multimodal medical assistant that leverages state-of-the-art AI to analyze images and voice input, providing professional, human-like medical responses. Built with FastAPI, Gradio, and advanced LLMs, it can:

- 🩺 Analyze medical images and answer health-related questions
- 🎤 Transcribe patient voice input to text
- 🗣️ Respond with natural, doctor-like speech
- 🌐 Easy-to-use web interface powered by Gradio

---

## 🚀 Features

- **Image Analysis:** Upload a photo (e.g., skin condition) and get a medical opinion
- **Voice Interaction:** Speak your symptoms/questions, get transcribed and analyzed
- **AI Doctor Response:** LLM-powered, context-aware, concise, and human-like answers
- **Text-to-Speech:** Doctor's response is spoken back to you

---

## 🛠️ Tech Stack

- Python 3.12+
- FastAPI
- Gradio
- Groq LLM API
- gTTS / ElevenLabs (Text-to-Speech)
- Whisper (Speech-to-Text)

---

## ⚡ Quick Start (Local)

1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/AI_DOCTOR.git
   cd AI_DOCTOR
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set environment variables:**
   - Create a `.env` file and add your API keys (e.g., `GROQ_API_KEY`)
4. **Run the app:**
   ```bash
   python -m ai_doctor.gradio_app
   # or
   uvicorn ai_doctor.gradio_app:app --host 0.0.0.0 --port 7860
   ```
5. **Open in browser:**
   - Visit [http://localhost:7860](http://localhost:7860)

---

## ☁️ Deployment

Supported on Render, Heroku, Fly.io, Google Cloud Run, and more.

**Render Example:**
```
Build Command: apt-get update && apt-get install -y portaudio19-dev && pip install -r requirements.txt
Start Command: PYTHONPATH=. uvicorn ai_doctor.gradio_app:app --host 0.0.0.0 --port $PORT
```

---

## 📁 Project Structure

```
ai_doctor/
  brain_of_the_doctor.py      # LLM and image analysis logic
  gradio_app.py               # Gradio web UI
  voice_of_the_doctor.py      # Text-to-speech
  voice_of_the_patient.py     # Audio recording & speech-to-text
requirements.txt
README.md
```

---


## 🙏 Credits

- [Gradio](https://gradio.app/)
- [Groq](https://groq.com/)
- [gTTS](https://pypi.org/project/gTTS/)
- [ElevenLabs](https://elevenlabs.io/)
- [OpenAI Whisper](https://github.com/openai/whisper)
- Help with [AI with Hussan YouTube channel](https://www.youtube.com/@AIwithHussan)

---

## 📜 License

MIT License. For educational and research use only. Not for real medical diagnosis.