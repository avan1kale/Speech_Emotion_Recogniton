# 🎙️ EchoSense – Speech Emotion Recognition

<div align="center">

### *AI-powered Speech Emotion Recognition using Deep Learning*

Detect human emotions from speech using a CNN-LSTM deep learning model. EchoSense supports both **audio file upload** and **real-time microphone recording** through a modern Flask web application.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

# 📖 Overview

EchoSense is a deep learning web application capable of recognizing emotions from speech.

The application allows users to:

- 🎤 Record voice directly from the browser
- 📁 Upload audio files
- 🧠 Predict emotion using a trained CNN-LSTM model
- 📊 Display confidence score
- ⚡ Get results instantly through an interactive web interface

---

# ✨ Features

- 🎙️ Live microphone recording
- 📂 Audio file upload
- 🤖 CNN + LSTM based emotion classification
- 🎵 Automatic WebM → WAV conversion using FFmpeg
- 📈 Confidence score visualization
- 🎨 Modern responsive UI
- ⚡ Real-time prediction without page refresh

---

# 🧠 Emotions Recognized

- 😄 Happy
- 😢 Sad
- 😠 Angry
- 😨 Fear
- 🤢 Disgust
- 😲 Surprise
- 😐 Neutral
- 😌 Calm

---

# 🛠 Tech Stack

### Backend

- Flask
- Python

### Deep Learning

- TensorFlow
- Keras
- NumPy
- Librosa

### Frontend

- HTML5
- CSS3
- JavaScript

### Audio Processing

- FFmpeg
- MediaRecorder API

---

# 📂 Project Structure

```text
EchoSense/
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── emotion_model.keras
├── label_encoder.pkl
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/EchoSense.git
```

---

## 2. Enter the project directory

```bash
cd EchoSense
```

---

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 5. Install FFmpeg

### Windows

Download FFmpeg:

https://ffmpeg.org/download.html

Extract it and add the **bin** folder to your system PATH.

Verify installation:

```bash
ffmpeg -version
```

---

## 6. Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# 🚀 How to Use

## Upload an Audio File

- Choose an audio file
- Click **Upload & Predict**
- View the predicted emotion and confidence score

---

## Live Recording

- Click **Start Recording**
- Speak into the microphone
- Click **Stop Recording**
- Wait for prediction

---

# 🧠 Model Pipeline

```text
Microphone / Audio File
            │
            ▼
      Audio Upload
            │
            ▼
     FFmpeg Conversion
            │
            ▼
     Feature Extraction
        (MFCC - 40)
            │
            ▼
     CNN + LSTM Model
            │
            ▼
 Emotion Prediction
            │
            ▼
 Confidence Score
            │
            ▼
  Interactive Web UI
```

---

# 📊 Dataset

The model was trained on the **RAVDESS Speech Emotion Dataset**.

Emotion classes:

- Neutral
- Calm
- Happy
- Sad
- Angry
- Fearful
- Disgust
- Surprised

---

# 💻 API Endpoints

| Endpoint | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Home page |
| `/predict` | POST | Predict emotion from uploaded audio |
| `/record` | POST | Predict emotion from live recording |

---

# 🤝 Fork & Run the Project

## Step 1

Fork this repository using the **Fork** button on GitHub.

---

## Step 2

Clone your fork.

```bash
git clone https://github.com/<your-username>/EchoSense.git
```

---

## Step 3

Move into the project.

```bash
cd EchoSense
```

---

## Step 4

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

## Step 5

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 6

Install FFmpeg.

Verify:

```bash
ffmpeg -version
```

---

## Step 7

Run the application.

```bash
python app.py
```

Visit

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

Add screenshots here.

Example:

```
screenshots/
│
├── home.png
├── recording.png
├── upload.png
└── prediction.png
```

---

# 🔮 Future Improvements

- User authentication
- Prediction history
- Model comparison
- Audio waveform visualization
- Emotion probability graph
- Cloud deployment
- Docker support
- REST API
- Dark / Light mode
- Mobile optimization

---

# 👨‍💻 Author

**Avani Kale**

Feel free to connect and contribute!

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

### ⭐ If you found this project useful, don't forget to star the repository!

Made with ❤️ using Flask & TensorFlow

</div>