#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def print_hello():
    """A function that returns a mesage"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def print_hbnb():
    """A function that returns another message"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def print_cmessage(text):
    """A function that prints a customized message"""
    return "C " + text.replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
