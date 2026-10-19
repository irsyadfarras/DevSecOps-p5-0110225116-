from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Selamat datang di API DevSecOps!", "status": "running"})

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json() or {}
    num1 = data.get('num1', 0)
    num2 = data.get('num2', 0)
    return jsonify({"result": num1 + num2})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # nosec B104
