# 🚀 PulsePoint AI

## 🏆 Hackathon
**ByteSize Sage AI Hackathon**  
*Master the Attention Economy with Generative AI*

---

## 📌 Problem Statement
Long-form educational and informational videos contain valuable insights, but today’s audiences prefer short, engaging, and easily consumable content. Manually identifying key moments and creating short clips is time-consuming and inefficient.

---

## 💡 Solution
**PulsePoint AI** is an AI-powered system that automatically converts long-form videos into short, high-impact reels by intelligently identifying important moments and clipping them.  
The platform helps creators, educators, and businesses maximize reach and engagement in the attention economy.

---

## ✨ Key Features
- Upload long-form video (lecture, podcast, talk, etc.)
- Automatic key-moment identification
- Generates multiple short reels from a single video
- Handles both short and long videos gracefully
- Robust error handling (no-audio / short clips)
- Simple and interactive Streamlit web interface

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit** – Web Interface
- **MoviePy** – Video Processing
- *(Planned Enhancements)* Whisper, Gemini API, Auto Captions

---

## ⚙️ How It Works
1. User uploads a long-form video
2. Audio is extracted (if available)
3. Key moments are identified
4. Video is clipped into multiple short reels
5. Reels are displayed and ready to download

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
---

## ▶️ How to Run the Project
```bash
pip install -r requirements.txt
python -m streamlit run app.py
```

## Demo Video
Working Demo (Screen Recording):
(https://drive.google.com/file/d/1bNvZ5925Vl68e_AxXwXx2sF7W1q1BDQd/view?usp=drive_link)

## Output

Automatically generates 3–5 short video reels
Each reel is suitable for social media sharing (Reels / Shorts)

## Future Enhancements

AI-based speech transcription (Whisper)
Emotion & sentiment-based clip selection
Auto captions generation
Vertical (9:16) reel formatting
Viral hook text generation using LLMs

## Developed and Created By
Mayank Aneja

