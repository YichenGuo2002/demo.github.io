# app.py
from flask import Flask, jsonify
from flask_cors import CORS

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

if __name__ == '__main__':
    app.run(debug=True)
