# 📖 AI Workflow Master Guide: From Zero to Pro

This guide explains how this AI Automation system works, designed for absolute beginners.

---

## ⚙️ 1. How the Workflow Works
1.  **Frontend (UI):** Users interact with a responsive glassmorphism dashboard.
2.  **Logic Engine (Flask):** The `process_workflow()` function in `app.py` acts as the traffic controller.
    *   **Keyword "Job"**: Triggers a heavy automation (AI -> DB -> Email).
    *   **Keyword "Help"**: Triggers a static support response (Saves API costs).
3.  **Database:** Uses SQLite (a local file) to keep a permanent log of all questions.
4.  **Webhooks**: External apps can send data to `/webhook` for automated logging.

---

## 📡 2. Deployment: Mobile & PC
The app is fully responsive. It uses **CSS Media Queries** to detect if you are on a phone or a laptop and automatically resizes the layout.
*   **Production Host:** Render.com
*   **Production Server:** Gunicorn (handles multiple users simultaneously).
*   **Dynamic Port:** The app detects the environment port automatically (`os.environ.get("PORT")`).

---

## ⚡ 3. Running out of Quota? (Adding Other LLMs)
If you hit your **Gemini Quota**, you can easily swap models. Here is how you would do it:

### Adding Groq (A very fast free alternative):
1. Get a key from [Groq Cloud](https://console.groq.com/).
2. In `app.py`, update `get_ai_response` to:
```python
from groq import Groq
client = Groq(api_key="your_groq_key")

def get_ai_response(user_input):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": user_input}]
    )
    return completion.choices[0].message.content
```

---

## 🚧 4. Challenges & Solutions Record
*   **Model 404 Error:** Solved by listing available models via a custom check script and matching the name `gemini-2.5-flash`.
*   **Vercel Crash (Error 500):** Solved by moving `init_db()` to the top level and ensuring Environment Variables are set.
*   **Port Conflicts:** Fixed by using `host='0.0.0.0'` and `os.environ.get("PORT")` for Render compatibility.

---
**Happy Automating!**
