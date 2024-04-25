from flask import Flask, request, jsonify
from flask_cors import CORS
import string
import random
import os

app = Flask(__name__)
CORS(app)  # Enable CORS

# Get the base URL from the environment variable
BASE_URL = os.environ.get('BASE_URL', 'https://flaskdb-mt6w.onrender.com')
# BASE_URL = os.environ.get('BASE_URL', 'localhost:5000') 

# In-memory data structure to store URL mappings
url_mappings = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    if short_url in url_mappings:
        return generate_short_url()
    return short_url
@app.route("/")
def home():
    return ("hi")
@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['longUrl']
    short_url = generate_short_url()
    url_mappings[short_url] = long_url
    short_url_with_base = f'{BASE_URL}/{short_url}'
    return jsonify({'shortUrl': short_url_with_base}), 201

if __name__ == '__main__':
    app.run(debug=True)