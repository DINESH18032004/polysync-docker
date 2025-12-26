# POLYSYNC: AN AI-DRIVEN FRAMEWORK FOR MULTILINGUAL VIDEO LOCALIZATION AND LIP-SYNCHRONIZED DUBBING

## 📌 Project Description
PolySync is a Docker-based AI pipeline for **multilingual video dubbing**.  
It automates speech transcription, translation, text-to-speech synthesis, and lip synchronization to generate localized videos efficiently.

---

## 🎯 Objectives
- Automate multilingual video localization
- Reduce manual dubbing effort
- Ensure accurate lip synchronization
- Provide easy deployment using Docker

---

## 🛠️ Technologies Used
- Python
- Docker & Docker Compose
- Whisper (ASR)
- Marian NMT (Translation)
- VITS (Text-to-Speech)
- Wav2Lip (Lip Sync)
- FFmpeg

---

## ⚙️ System Requirements
- Docker
- Docker Compose
- Minimum 8 GB RAM
- GPU (optional but recommended)

---

## 📂 Project Structure
<img width="1536" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/674bec4b-fac1-4fac-a380-b80998bc169b" />

## 📥 Input
- Input should be a video file (`.mp4`)
- Place the video inside the `input/` directory
- Sample file: `sample_input.mp4` (5–10 seconds)
  
## 📤 Output
- The localized output video will be generated in the `output/` directory
- Output format: `.mp4`
- The video contains translated speech with lip synchronization

## 📈 Applications

- Multilingual video dubbing
- Online education platforms
- Media localization
- Research and academic use

## 📊 Results
- Successfully generated multilingual dubbed videos from input video files
- Accurate speech transcription and translation across supported languages
- Natural-sounding synthesized speech using neural TTS
- Effective lip synchronization preserving speaker facial movements
- End-to-end pipeline executed smoothly using Docker containers

---

## 🌍 Impact
- Reduces manual effort and cost involved in video dubbing
- Enables faster localization of educational and media content
- Improves accessibility for non-native language audiences
- Demonstrates practical application of AI in multimedia processing
- Useful for academic research and real-world multilingual systems

