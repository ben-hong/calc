from flask import Flask, request
import operations

app = Flask(__name__)

@app.route('/add')
def add():
    a = request.args["a"]
    b = request.args["b"]

    add = operations.add(int(a), int(b))

    return str(add) 

@app.route('/sub')
def sub():
    a = request.args["a"]
    b = request.args["b"]

    sub = operations.sub(int(a), int(b))
    return str(sub)

@app.route('/mult')
def mult():
    a = request.args["a"]
    b = request.args["b"]

    mult = operations.mult(int(a), int(b))
    return str(mult)

@app.route('/div')
def div():
    a = request.args["a"]
    b = request.args["b"]

    div = operations.div(int(a), int(b))
    return str(div)
