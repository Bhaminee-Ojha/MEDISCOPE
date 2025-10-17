# 🩺 MediScope — AI-Powered Symptom Analyzer

**MediScope** is an AI-powered web app that takes user symptom inputs and provides possible health conditions, severity levels, and recommendations — powered by **Google Gemini**.  
⚠️ *For educational purposes only. Not a substitute for professional medical advice.*

---

## 🚀 Features

- 🧠 **LLM-Powered Analysis** — Uses Gemini to infer probable diseases and advice from symptoms.
- 🌍 **Interactive Dashboard** — Displays symptom clusters on a map.
- 🔐 **Login System** — Basic Firebase authentication (email/password).
- 🗄️ **Firestore Integration** — Stores user queries and timestamps for analytics.
- 🎨 **Clean UI/UX** — Simple, responsive, and beginner-friendly.

---

## 🧩 Architecture Overview

**Frontend**
- `index.html`: User input form.
- `dashboard.html`: Visualization using Leaflet.js map.

**Backend**
- `app.py`: Flask API — receives symptoms → queries Gemini → returns JSON.
- Firestore stores user data and responses.

**LLM**
- Google Gemini (`gemini-2.0-flash`) used via `google-generativeai`.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | HTML, CSS, JS, Leaflet.js |
| Backend | Python, Flask |
| AI Model | Google Gemini |
| Database | Firebase Firestore |
| Auth | Firebase Authentication |

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/YOUR_USERNAME/MediScope.git
cd MediScope
