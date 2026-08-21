from flask import Flask, jsonify, request, make_response
import os, threading, time

app = Flask(__name__, instance_relative_config=True)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify(message="Hello world!")

@app.route('/upper', methods=['GET'])
def fun_upper():

    a = request.args.get('a', type=str)

    if a is not None:

        res = a.upper()
        operation = f"upper({a})={res}"
        last_operation(operation)

        return make_response(jsonify(s=res), 200)
    else:
        return make_response(jsonify({"error":"Invalid input"}), 400)

@app.route('/lower', methods=['GET'])
def fun_lower():

    a = request.args.get('a', type=str)

    if a is not None:
        res = a.lower()
        operation = f"lower({a})={res}"
        last_operation(operation)
        return make_response(jsonify(s=res), 200)
    else:
        return make_response(jsonify({"error":"Invalid input"}), 400)

@app.route('/concat', methods=['GET'])
def fun_concat():

    a = request.args.get('a', type=str)
    b = request.args.get('b', type=str)

    if a is None or b is None:
        return make_response(jsonify({"error":"Invalid input"}), 400)
    else:
        res = a+b
        operation = f"concat({a},{b})={res}"
        last_operation(operation)
        return make_response(jsonify(s=res), 200)

@app.route('/reduce', methods=['GET'])
def fun_reduce():

    op = request.args.get('op', type=str)
    lst = request.args.get('lst', type=str)

    if op is None or lst is None:
        return make_response(jsonify({"error":"Invalid Input"}), 400)
    
    
    lst = eval(lst)

    if not isinstance(lst, list) or len(lst) == 0:
        return make_response(jsonify({"error": "Invalid list"}), 400)
    
    if op == 'add':
        res = lst[0]
        for i in lst[1:]:
            res += i 

    elif op == 'sub':
        res = lst[0]
        for i in lst[1:]:
            res -= i

    elif op == 'div':
        res = lst[0]
        for i in lst[1:]:
            res /= i

    elif op == 'concat':
        res = lst[0]
        for i in lst[1:]:
            res += i

    elif op == 'mul':
        res = lst[0]
        for i in lst[1:]:
            res *= i
    else: 
        return make_response(jsonify({"error":"Invalid input"}), 400)
    
    operation = f"reduce({op},{lst})={res}"
    last_operation(operation)

    return make_response(jsonify(s=res), 200)

@app.route('/crash', methods=['GET'])
def fun_crash():
    def second_crash():
        time.sleep(2)
        os._exit(0)
    
    thread = threading.Thread(target=second_crash)
    thread.start()
    res = request.host
    operation = f"crash={res}"
    last_operation(operation)
    return make_response(jsonify(s=res), 200)

@app.route('/last', methods=['GET'])
def fun_last():
    with open("data.txt", "r") as file:
        last_operation = file.readline()

    return make_response(jsonify(s=last_operation), 200)

def last_operation(operation):

    with open("data.txt", "w") as file:
        file.write(operation)

if __name__ == '__main__':
    app.run(debug=True)