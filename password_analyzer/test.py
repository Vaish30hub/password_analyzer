
print("Step 1: Python is running!")

try:
    from flask import Flask
    print("Step 2: Flask imported successfully!")
except Exception as e:
    print("❌ Flask import failed:", e)
    print("Run: pip install flask")
    input("Press Enter to exit...")
    exit()

app = Flask(__name__)

@app.route("/")
def home():
    return "🎉 SUCCESS! Flask is LIVE on http://127.0.0.1:8000"

if __name__ == "__main__":
    print("Step 3: Starting Flask server...")
    print("👉 Open your browser and go to: http://127.0.0.1:8000")
    app.run(host="127.0.0.1", port=8000, debug=True)
