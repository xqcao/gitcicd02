from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/api/users', methods=['GET'])
def findAllUsers():
    uu = [{"username": "admin", "email": "admin@example.com"},
          {"username": "cat", "email": "cat@example.com"}]
    return jsonify(uu)


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
