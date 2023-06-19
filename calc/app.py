from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_params():
    """takes two get request arguments and adds them together."""
    
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = add(a,b)
    return str(result)

@app.route("/sub")
def sub_params():
    """takes two get request arguments and subtracts them."""
    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = sub(a,b)
    return str(result)

@app.route("/mult")
def mult_params():
    """takes two get request arguments and multiplies them."""

    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = mult(a,b)
    return str(result)

@app.route("/div")
def div_params():
    """takes two get request arguements and divides them."""

    a = int(request.args.get("a"))
    b = int(request.args.get('b'))
    result = div(a,b)
    return str(result)


#part 2 (additional study)

operators = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}

@app.route('/math/<oper>')
def do_math(oper):
    """uses var oper to perform designated math function on targets a and b from request.args"""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))

    result = operators[oper](a, b)

    return str(result)