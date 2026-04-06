from flask import Flask, request, jsonify
from flask_cors import CORS
from zxcvbn import zxcvbn  # Industry standard checker
import secrets             # Secure random generator
import string              # Helper for characters

app = Flask(__name__)
CORS(app)

# --- ROUTE 1: ANALYZE STRENGTH ---
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    pwd = data.get('password', '')
    
    if not pwd:
        return jsonify({"entropy": 0, "strength": "None", "feedback": "Enter a password"})

    # Advanced analysis using zxcvbn
    results = zxcvbn(pwd)
    
    score_labels = ["Very Weak", "Weak", "Fair", "Strong", "Very Strong"]
    strength_label = score_labels[results['score']]
    
    # Get specific feedback (like "This is a top 10 common password")
    warning = results['feedback']['warning']
    suggestion = results['feedback']['suggestions'][0] if results['feedback']['suggestions'] else ""
    full_feedback = f"{warning}. {suggestion}".strip() if warning else "This is a safe password!"
    
    return jsonify({
        "entropy": round(results['guesses_log10'], 2),
        "strength": strength_label,
        "feedback": full_feedback,
        "score": results['score'] # 0 to 4
    })

# --- ROUTE 2: GENERATE PASSWORD ---
@app.route('/generate', methods=['GET'])
def generate():
    # Character pool: Uppercase, Lowercase, Digits, and Symbols
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Securely pick 16 random characters
    password = ''.join(secrets.choice(alphabet) for i in range(16))
    
    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(port=5000, debug=True)