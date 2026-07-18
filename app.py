from flask import Flask, render_template, request
import os
import librosa
import numpy as np
import tensorflow as tf
import pickle
import subprocess
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

model = tf.keras.models.load_model("emotion_model.keras")
with open("label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

#function to extract features from audio file
def extract_features(audio_path):

    audio, sample_rate = librosa.load(audio_path, sr=None)

    mfcc = librosa.feature.mfcc(
        y=audio,
        sr=sample_rate,
        n_mfcc=40
    )

    mfcc = mfcc.T

    MAX_LEN = 200

    if mfcc.shape[0] < MAX_LEN:
        pad_width = MAX_LEN - mfcc.shape[0]
        mfcc = np.pad(
            mfcc,
            ((0, pad_width), (0, 0)),
            mode="constant"
        )
    else:
        mfcc = mfcc[:MAX_LEN, :]

    mfcc = np.expand_dims(mfcc, axis=0)

    return mfcc


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    audio = request.files["audio"]

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        audio.filename
    )

    audio.save(filepath)

    features = extract_features(filepath)

    prediction = model.predict(features)

    predicted_class = np.argmax(prediction)

    emotion = encoder.inverse_transform([predicted_class])[0]

    confidence = np.max(prediction) * 100

    return f"""
    <h2>Prediction Result</h2>

    <h3>Emotion : {emotion}</h3>

    <h3>Confidence : {confidence:.2f}%</h3>

    <a href="/">Predict Another</a>
    """

@app.route("/record", methods=["POST"])
def record():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    audio = request.files["audio"]

    webm_path = os.path.join(
    app.config["UPLOAD_FOLDER"],
    f"{timestamp}.webm"
    )

    wav_path = os.path.join(
    app.config["UPLOAD_FOLDER"],
    f"{timestamp}.wav"
    )

    audio.save(webm_path)

    subprocess.run([
        "ffmpeg",
        "-y",
        "-i", webm_path,
        wav_path
    ])

    features2 = extract_features(wav_path)
    prediction2 = model.predict(features2)
    predicted_class2 = np.argmax(prediction2)
    emotion2 = encoder.inverse_transform([predicted_class2])[0]
    confidence2 = float(np.max(prediction2) * 100)

    return jsonify({
    "emotion": emotion2,
    "confidence": round(confidence2, 2)
    })

if __name__ == "__main__":
    app.run(debug=True)