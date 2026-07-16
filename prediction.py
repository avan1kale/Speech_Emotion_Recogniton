import librosa
import numpy as np
import tensorflow as tf
import pickle

model = tf.keras.models.load_model("E:\DEEP LEARNING\Speech emotion recognition\emotion_model.keras")

with open("E:\DEEP LEARNING\Speech emotion recognition\label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

audio_path = "E:\\DEEP LEARNING\\Speech emotion recognition\\dataset\\Actor_04\\03-01-01-01-01-01-04.wav"

audio, sample_rate = librosa.load(audio_path, sr=None)
mfcc = librosa.feature.mfcc(
    y=audio,
    sr=sample_rate,
    n_mfcc=40
)
mfcc = mfcc.T

# Pad or Truncate MFCC Features
MAX_LEN = 200

if mfcc.shape[0] < MAX_LEN:
    pad_width = MAX_LEN - mfcc.shape[0]
    mfcc = np.pad(mfcc, ((0, pad_width), (0, 0)), mode='constant')
else:
    mfcc = mfcc[:MAX_LEN, :]

mfcc = np.expand_dims(mfcc, axis=0)

 
prediction = model.predict(mfcc)
predicted_class = np.argmax(prediction)
emotion = encoder.inverse_transform([predicted_class])[0]
confidence = np.max(prediction) * 100


# Output
print("Predicted Emotion :", emotion)
print(f"Confidence : {confidence:.2f}%")