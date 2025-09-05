from flask import Flask, jsonify, render_template
import socket
import os

app = Flask(__name__)

def fetchDetails():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route("/")
def home():
    app_name = os.getenv("APP_NAME", "Flask-App")
    return f"🚀 Hello from {app_name}!"

@app.route("/health")
def health_check():
    return jsonify(status="Healthy")

@app.route("/details")
def details():
    hostname, ip = fetchDetails()
    app_name = os.getenv("APP_NAME", "Flask-App")
    return render_template("index.html", hostname=hostname , ip=ip, app_name=app_name)

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it works inside Docker
    app.run(host="0.0.0.0", port=5000, debug=True)
