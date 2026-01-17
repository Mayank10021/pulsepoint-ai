# 🎥 PulsePoint AI

PulsePoint AI is an AI-powered video processing tool that automatically extracts the most emotional and impactful moments from long videos and converts them into short, shareable reels.

This project is designed for hackathons and content creators who want quick highlights without manual editing.

---

## 🚀 Features

- 🎧 Extract audio from video automatically
- 📝 Transcribe speech into text
- ❤️ Detect emotional / important moments
- ✂️ Generate short video clips (reels)
- 🖥️ Simple Streamlit-based UI
- 🧩 Modular and extensible architecture

---

## 🛠️ Tech Stack

- Python 3.9+
- Streamlit
- MoviePy
- FFmpeg
- (Future-ready for OpenAI Whisper / Gemini)

---

## 📂 Project Structure

pulsepoint-ai/
├── app.py # Streamlit UI
├── pipeline.py # Main processing pipeline
├── extract_audio.py # Audio extraction logic
├── transcribe.py # Speech-to-text module
├── emotion_detector.py # Key moment detection
├── clip_generator.py # Reel generation
├── output_clips/ # Generated reels
├── requirements.txt # Dependencies
├── README.md # Project documentation
└── LICENSE # Open-source license

yaml
Copy code

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
2️⃣ Run the application
bash
Copy code
streamlit run app.py
3️⃣ Upload a video
Supported format: .mp4

Click Process Video

Reels will be generated automatically

🧠 How It Works (Pipeline)
Audio Extraction

Extracts audio from the uploaded video.

Transcription

Converts speech to text (currently dummy, Whisper-ready).

Emotion Detection

Finds emotionally important timestamps.

Clip Generation

Cuts short reels from original video.

🏆 Hackathon Use Case
🎬 Content creators

🎙️ Podcast highlights

🎓 Educational summaries

📢 Marketing reels

📰 News highlights

🔮 Future Enhancements
Real-time Whisper transcription

Emotion detection using ML models

Auto captions & subtitles

Vertical (9:16) Instagram/TikTok reels

Cloud deployment

👨‍💻 Team
Project developed for hackathon submission

Fully open-source and customizable

📜 License
This project is licensed under the MIT License.
See the LICENSE file for details.

sql
Copy code

---

# 📜 LICENSE (English – MIT License)

Create a file named **LICENSE** and paste this 👇

```txt
MIT License

Copyright (c) 2025 PulsePoint AI Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
