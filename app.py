from flask import Flask, request, jsonify
from ml_model import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Iron Man Chatbot!"

@app.route('/get_response', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

