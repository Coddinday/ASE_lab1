from flask import Flask, jsonify

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello world!")

if __name__ == '__main__':
    app.run(debug=True)