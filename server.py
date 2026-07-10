from flask import Flask, jsonify
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify(status='ok')

@app.route('/api/hello')
def hello():
    return jsonify(message='Hello, world!', time=datetime.now(timezone.utc).isoformat())

if __name__ == '__main__':
    app.run(port=3000)