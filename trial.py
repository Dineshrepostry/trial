from flask import Flask, request, jsonify

app = Flask(__name__)

# API endpoint for GET request
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello!'

# API endpoint for POST request
@app.route('/greet', methods=['POST'])
def greet():
    data = request.get_json()
    name = data.get('name')
    if name:
        return f'Hello, {name}!'
    else:
        return 'Please provide a name in the request body.', 400

if __name__ == '__main__':
    app.run(debug=True)
