## Full-Stack Password Security & Entropy Analyzer

A lightweight, full-stack web application designed to evaluate password strength using realistic security metrics (entropy, dictionary checks, pattern matching) rather than arbitrary character-count rules. Includes a cryptographically secure random password generator.

---

## ✨ Features

* **Realistic Strength Evaluation:** Powered by Dropbox's `zxcvbn` library to detect common keyboard patterns, sequences, and dictionary words.
* **Instant Visual Feedback:** Real-time strength metering, color-coded status bar, and specific remediation advice.
* **Cryptographically Secure Generator:** Generates high-entropy 16-character passwords using Python's `secrets` module.
* **RESTful Architecture:** Clear separation of concerns with a Python backend API and a vanilla JavaScript frontend.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-CORS, `zxcvbn`, `secrets`
* **Frontend:** HTML5, CSS3, JavaScript (ES6+ / Fetch API)
* **Tools:** Visual Studio Code, Git

---

## 📁 Project Structure

```text
PasswordProject/
│
├── app.py          # Flask backend (analysis & generation API)
├── index.html      # Frontend markup & asynchronous UI script
├── style.css       # UI styling and progress transitions
└── README.md       # Project documentation

🚀 Getting Started
Prerequisites
Python 3.8+ installed on your machine

VS Code (recommended: Live Server extension)

1. Clone the Repository
Bash
git clone [https://github.com/your-username/password-security-analyzer.git](https://github.com/your-username/password-security-analyzer.git)
cd password-security-analyzer
2. Set Up the Backend
Create a virtual environment (optional but recommended) and install dependencies:

Bash
pip install flask flask-cors zxcvbn
Start the Flask server:

Bash
python app.py
The server will start at http://127.0.0.1:5000.

3. Launch the Frontend
Open index.html in VS Code.

Right-click and choose "Open with Live Server" (or simply double-click index.html in your file explorer).

📡 API Reference
POST /analyze
Analyzes password complexity and returns feedback.

Body: {"password": "<string>"}

Response:

JSON
{
  "entropy": 3.45,
  "feedback": "This is a top-10 common password. Add another word or two.",
  "score": 0,
  "strength": "Very Weak"
}
GET /generate
Generates a random, high-entropy 16-character password.

Response:

JSON
{
  "password": "4k#L9!zP2q&R5m$X"
}
📄 License
This project is licensed under the MIT License — see the LICENSE file for details.
