#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask
from flask import render_template

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


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def print_pythonmessage(text):
    """A function that prints another customized message
    with a default option"""
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def print_number(n):
    """A function that prints a message only if n is int"""
    return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """A function that renders a HTML page only if n is int"""
    return render_template("5-number.html", number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
