# 🚀 Streamlit NLP App

A simple Streamlit-based web application for text processing and prediction using a trained vectorizer/model.

---

## 📁 Project Structure
.
├── src/
│ └── streamlit_app.py
├── requirements.txt
├── README.md


---

## ⚙️ Features

- Interactive text input via Streamlit UI
- Text vectorization using a trained vectorizer
- Prediction / analysis output
- Lightweight and fast deployment

---

## 📦 Dependencies
streamlit
scikit-learn
joblib
numpy
pandas

(See requirements.txt for full list)

⚠️ Notes
Avoid uploading .joblib / .pkl files directly (may be flagged as unsafe)
Prefer loading models dynamically or recreating vectorizers in code
