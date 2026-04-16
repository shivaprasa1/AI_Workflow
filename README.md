# 🤖 AI Workflow Automation System

A powerful, full-stack AI Automation pipeline built with Python (Flask), Google Gemini AI, and SMTP. This system processes intelligent queries, tracks history, and automates email responses based on specialized workflow triggers.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)
![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)
![Deployment](https://img.shields.io/badge/deployment-Render-blue.svg)

## 🎯 Key Features
*   **Intelligent Automation:** Specialized triggers for "Job" and "Help" tasks.
*   **Multi-Model Ready:** Currently powered by Google Gemini, but architected for easy swapping (Groq, OpenAI, etc.).
*   **Audit Logging:** Persistent query storage via SQLite.
*   **Automated Emailing:** Instant SMTP-based notifications.
*   **Webhooks:** Dedicated `/webhook` endpoint for third-party tool integration.
*   **Responsive UI:** Optimized glassmorphism design for Mobile/Tablet/Desktop.

## 🛠️ Tech Stack
*   **Backend:** Flask (Python) + Gunicorn (Production Server)
*   **AI Engine:** Google Gemini (1.5 Flash / 2.5 Flash)
*   **Database:** SQLite3
*   **Frontend:** HTML5, CSS3, JavaScript
*   **Deployment:** Render / Vercel (Configured)

## 🚀 Quick Start

1. **Clone the repo:**
   ```bash
   git clone https://github.com/shivaprasa1/AI_Workflow.git
   cd AI_Workflow
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment (`.env`):**
   ```env
   GEMINI_API_KEY=your_key
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password
   ```

4. **Run Locally:**
   ```bash
   python app.py
   ```

## 🌐 Deployment (Render)
1. Create a **Web Service** on Render.
2. Build Command: `pip install -r requirements.txt`
3. Start Command: `gunicorn app:app`
4. Add your `.env` variables in the dashboard.

## 💡 Switching AI Providers
If you reach your Gemini quota, the system is designed to be modular. You can easily swap to **Groq** or **OpenAI** by updating the `get_ai_response` function in `app.py`.

---
Built with ❤️ by [Shiva Prasad](https://github.com/shivaprasa1)
