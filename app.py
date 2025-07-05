import streamlit as st
import os
from scripts.predict_emotion import predict_emotion

st.set_page_config(page_title="VoiceGuardian - Emotion Detection", layout="centered")
st.title("🎙️ VoiceGuardian – Emotion Detection from Speech")
st.markdown("Upload a short voice clip (.wav) and get your detected emotion using AI-powered deep learning.")

uploaded_file = st.file_uploader("🎧 Upload a .wav file", type=["wav"])

if uploaded_file:
    with open("temp.wav", "wb") as f:
        f.write(uploaded_file.read())
    st.audio("temp.wav", format="audio/wav")

    if st.button("🔍 Predict Emotion"):
        result = predict_emotion("temp.wav")
        st.success(f"🧠 Detected Emotion: **{result.upper()}**")

        # Optional: Emoji feedback
        emojis = {
            "happy": "😄", "sad": "😢", "angry": "😡", "calm": "😌",
            "neutral": "😐", "fearful": "😨", "surprised": "😲", "disgust": "🤢"
        }
        if result.lower() in emojis:
            st.markdown(f"**You sound {result.lower()} {emojis[result.lower()]}**")
    