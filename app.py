from flask import Flask, request, jsonify
import string
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# In-memory data structure to store URL mappings
url_mappings = {}

def generate_short_url():
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for _ in range(6))
    if short_url in url_mappings:
        return generate_short_url()
    return short_url

@app.route('/api/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['longUrl']
    short_url = generate_short_url()
    url_mappings[short_url] = long_url
    return jsonify({'shortUrl': f'http://localhost:5000/{short_url}'}), 201

if __name__ == '__main__':
    app.run(debug=True)