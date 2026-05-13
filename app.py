from flask import Flask, render_template, request, jsonify
import base64
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    data = request.get_json()
    if 'image' in data:
        img_data = data['image'].split(",")[1]
        with open("captured_image.png", "wb") as f:
            f.write(base64.b64decode(img_data))
        print("Image captured and saved!")
    return jsonify({"status": "success"})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
