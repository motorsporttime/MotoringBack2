from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
app.logger.info("Flask app started successfully.")

@app.route('/api/schedule')
def schedule():
    return jsonify([])

@app.route('/api/results')
def results():
    return jsonify([])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)