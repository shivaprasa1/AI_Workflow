import os
import sqlite3
import smtplib
import google.generativeai as genai
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# --- Gemini AI Configuration ---
# Keeping the currently working configuration
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Using the model name requested/confirmed working
model = genai.GenerativeModel("gemini-2.5-flash")

# --- Database Setup ---
DB_PATH = "database.db"

def init_db():
    """Initializes the SQLite database and creates the necessary table."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            response TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_query(query, response):
    """Saves a query and its corresponding AI response to the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO insights (query, response) VALUES (?, ?)', (query, response))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Database Error: {e}")

# --- Email Automation ---
def send_email(to_email, subject, message_content):
    """Sends an automated email using Gmail SMTP."""
    try:
        sender_email = os.getenv("EMAIL_USER")
        sender_password = os.getenv("EMAIL_PASS")
        
        if not sender_email or not sender_password:
            print("Email credentials missing in .env")
            return False

        msg = MIMEMultipart()
        msg['From'] = f"AI Workflow Automator <{sender_email}>"
        msg['To'] = to_email
        msg['Subject'] = subject
        
        body = f"Hello,\n\nYour automated AI insight is ready:\n\n---\n{message_content}\n---\n\nBest regards,\nAI Workflow System"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False

# --- Core Business Logic ---
def get_ai_response(user_input):
    """Calls the Gemini API to generate a response."""
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        error_msg = f"Raw AI Error: {str(e)}"
        print(error_msg)
        return error_msg

def process_workflow(query, email=None):
    """
    Handles the automation logic based on query content.
    Workflow: Input -> Logic -> AI -> DB -> Email -> Response
    """
    query_lower = query.lower()
    
    # 1. SPECIAL WORKFLOW: Job Automation
    if "job" in query_lower:
        ai_response = get_ai_response(query)
        save_query(query, ai_response)
        
        email_status = "Not sent"
        if email:
            if send_email(email, f"Job Automation: {query[:30]}", ai_response):
                email_status = "Sent successfully"
        
        return {
            "status": "Job workflow triggered",
            "ai_response": ai_response,
            "email_status": email_status
        }
    
    # 2. SPECIAL WORKFLOW: Support/Help
    elif "help" in query_lower:
        return {
            "status": "Support workflow triggered",
            "ai_response": "How can I assist you today? You can ask about 'jobs' to trigger our automation workflow.",
            "email_status": "No email needed"
        }
    
    # 3. DEFAULT WORKFLOW: Normal AI response
    else:
        ai_response = get_ai_response(query)
        save_query(query, ai_response)
        return {
            "status": "Standard query processed",
            "ai_response": ai_response,
            "email_status": "Optional email not triggered" if not email else "Email sent" if send_email(email, "Your AI Response", ai_response) else "Email failed"
        }

# --- Routes ---

@app.route('/')
def index():
    """Renders the main UI."""
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    """Main API endpoint for processing user queries."""
    data = request.json
    query = data.get('query', '').strip()
    email = data.get('email', '').strip()

    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Execute workflow logic
    result = process_workflow(query, email)
    return jsonify(result)

@app.route('/history', methods=['GET'])
def history():
    """Fetches all past queries and responses from the database."""
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM insights ORDER BY timestamp DESC')
        rows = cursor.fetchall()
        conn.close()
        
        history_list = [dict(row) for row in rows]
        return jsonify(history_list)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/webhook', methods=['POST'])
def webhook():
    """External webhook endpoint to receive third-party data."""
    data = request.json
    print(f"\n[WEBHOOK RECEIVED] at {datetime.now()}")
    print(f"Data: {data}\n")
    return jsonify({"status": "Webhook received", "timestamp": str(datetime.now())})

init_db()

if __name__ == '__main__':
    app.run(debug=True)
