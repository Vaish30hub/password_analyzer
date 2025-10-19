
import os
from flask import Flask, render_template, request, jsonify


print("\n" + "="*60)
print("🚀 FLASK APP STARTING...")
print("Current Directory:", os.getcwd())
print("Files in this folder:", os.listdir("."))
print("Templates folder exists:", os.path.exists("templates"))
if os.path.exists("templates"):
    print("Files in templates:", os.listdir("templates"))
print("Static folder exists:", os.path.exists("static"))
print("Utils folder exists:", os.path.exists("utils"))
print("="*60)


app = Flask(__name__)


try:
    from utils.password_checker import check_strength, check_breach
    print("✅ Successfully imported 'password_checker.py'")
except Exception as e:
    print(f"❌ Import failed: {e}")
    print("💡 Using dummy functions for testing...")

    def check_strength(password):
        return "Medium", ["Strength check not available"]

    def check_breach(password):
        return False


@app.route("/")
def index():
    return render_template("index.html") 

@app.route("/test")
def test():
    return """
    <html>
    <body style="text-align: center; margin-top: 100px;">
        <h1 style="color: #007bff;">✅ Test Route Works!</h1>
        <p>If you see this, Flask is receiving requests.</p>
        <p><a href="/">← Back Home</a></p>
    </body>
    </html>
    """


@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        password = data.get("password", "").strip()

        if not password:
            return jsonify({"error": "Password required"}), 400

        strength, feedback = check_strength(password)

       
        if len(password) < 8 or "123" in password or password.lower() in ["password", "admin", "123456", "qwerty", "letmein"]:
            breach_status = "⚠️ Found in data breaches"
        else:
           
            breach_status = "✅ Not found in known breaches"

        return jsonify({
            "strength": strength,
            "feedback": feedback,
            "breach": breach_status
        })
    except Exception as e:
        print(f"❌ Error in /analyze: {e}")
        return jsonify({"error": "Server error", "msg": str(e)}), 500

if __name__ == "__main__":
    print("🔧 Starting Flask server on http://127.0.0.1:8000")
    print("💡 Keep this window open and visit http://127.0.0.1:8000 in your browser")
    print("❌ Do not click links from chat — manually type the URL\n")
    
    app.run(
        host="127.0.0.1",
        port=8000,
        debug=True,
        use_reloader=True,
        threaded=True
    )






