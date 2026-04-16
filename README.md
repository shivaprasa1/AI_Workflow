# 🤖 AI Workflow Automation System

A powerful, full-stack AI Automation pipeline built with Python (Flask), Google Gemini AI, and SMTP. This system processes intelligent queries, tracks history, and automates email responses based on specialized workflow triggers.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-brightgreen.svg)
![Framework](https://img.shields.io/badge/framework-Flask-lightgrey.svg)

## 🎯 Key Features
*   **Intelligent Automation:** Specialized triggers for "Job" and "Help" tasks to streamline workflows.
*   **Google Gemini Integration:** Leverages cutting-edge LLMs for high-quality reasoning.
*   **Audit Logging:** Every query and response is persistently stored in an SQLite database.
*   **Automated Emailing:** Instant SMTP-based email notifications for completed tasks.
*   **External Webhooks:** Dedicated endpoint (`/webhook`) for receiving data from third-party apps.
*   **Responsive UI:** Premium glassmorphism design fully optimized for Mobile and Desktop.

## 🛠️ Tech Stack
*   **Backend:** Flask (Python)
*   **AI Engine:** Google Gemini 1.5 Flash
*   **Database:** SQLite3
*   **Frontend:** Vanilla HTML5, CSS3, JavaScript
*   **Deployment:** Vercel (Ready)

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

3. **Configure Environment:**
   Create a `.env` file and add your keys:
   ```env
   GEMINI_API_KEY=your_key_here
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_app_password_here
   ```

4. **Run Locally:**
   ```bash
   python app.py
   ```

## 🌐 Deployment
This project is configured for **Vercel**. Connect your GitHub repo to Vercel, add your environment variables, and click Deploy.

---
Built with ❤️ by [Shiva Prasad](https://github.com/shivaprasa1)
