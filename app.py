import os
import base64
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from datetime import datetime
from werkzeug.utils import secure_filename

# Load environment variables from .env file
load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
BRANCH = "main"

app = Flask(__name__)

@app.route('/api/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    original_filename = secure_filename(file.filename)
    extension = os.path.splitext(original_filename)[1]  # example: .jpg, .png
    file_content = file.read()
    file_size = len(file_content)

    # Format: timestamp-size.extension
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{timestamp}-{file_size}{extension}"
    filepath = f"images/{new_filename}"

    # Encode file content to base64
    encoded_content = base64.b64encode(file_content).decode('utf-8')

    # GitHub API URL
    github_api_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{filepath}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "message": f"upload {new_filename}",
        "content": encoded_content,
        "branch": BRANCH
    }

    # Send PUT request to GitHub
    response = requests.put(github_api_url, json=data, headers=headers)
    if response.status_code in [200, 201]:
        raw_url = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}/{filepath}"
        return jsonify({"success": True, "url": raw_url})
    else:
        return jsonify({
            "success": False,
            "error": response.json()
        }), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
