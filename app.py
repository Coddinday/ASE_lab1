from flask import Flask, jsonify, request, make_response

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello world!")

@app.route('/upper', methods=['GET'])
def fun_upper():

    a = request.args.get('a', type=str)

    if a is not None:

        res = a.upper()
        return make_response(jsonify(s=res), 200)
    else:
        return make_response(jsonify({"error":"Invalid input"}), 400)

@app.route('/lower', methods=['GET'])
def fun_lower():

    a = request.args.get('a', type=str)

    if a is not None:
        res = a.lower()
        return make_response(jsonify(s=res), 200)
    else:
        return make_response(jsonify({"error":"Invalid input"}), 200)






if __name__ == '__main__':
    app.run(debug=True)