# app.py
from flask import Flask, jsonify
from flask_cors import CORS
from scraper2 import getMainTitle

app = Flask(__name__)
CORS(app)

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {
        'id': 1,
        'message': 'Hello from the backend!',
        'items': ['apple', 'banana', 'cherry'],
        'status':'success'
    }
    return jsonify(sample_data)

@app.route('/news', methods=['GET'])
def get_data_2():
    sample_data = getMainTitle()
    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)
