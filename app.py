from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello! This is my Professional Server on Render</h1><p>Status: Online</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
