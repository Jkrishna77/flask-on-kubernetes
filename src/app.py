from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from Flask Application!"

@app.route("/health")
def health_check():
    return jsonify(status="Healthy")

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it works inside Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
