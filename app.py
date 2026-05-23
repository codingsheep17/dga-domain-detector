import streamlit as st
import joblib
from tensorflow.keras.models import load_model

# Load model + vectorizer
model = load_model("dga_model.keras")
vectorizer = joblib.load("vectorizer.joblib")

# UI
st.set_page_config(page_title="DGA Detector", page_icon="🛡️")

st.title("🛡️ Malware Domain (DGA) Detector")
st.write("Enter a domain name to check if it's malicious or legit.")

domain = st.text_input("Enter domain (e.g., google.com)")

# Prediction
if st.button("Check Domain"):
    if domain.strip() == "":
        st.warning("Please enter a domain.")
    else:
        seq = vectorizer([domain])
        pred = model.predict(seq)[0][0]

        st.subheader("Result:")

        if pred > 0.5:
            st.error(f"⚠️ Malicious (DGA) — Confidence: {pred:.2f}")
        else:
            st.success(f"✅ Legit Domain — Confidence: {1 - pred:.2f}")

        with st.expander("Details"):
            st.write(f"Raw score: {pred}")