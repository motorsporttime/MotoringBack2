from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/schedule')
def schedule():
    return jsonify([])

@app.route('/api/results')
def results():
    return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
