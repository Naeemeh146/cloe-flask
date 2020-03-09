from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_whale():
    A = request.args.get('a')
    B = request.args.get('b')
    if A is not None and B is not None:
        return str(A + B)
    return "No Input"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')