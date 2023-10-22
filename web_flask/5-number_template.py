#!/usr/bin/python3
"""
5-number_template module
This module contains a script to start the flask web application
"""


from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """
        Flask route at root (http://0.0.0.0:5000/).
        Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
        Flask route at /hbnb (http://0.0.0.0:5000/).
        Displays 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
        Flask route at /c/<text> (http://0.0.0.0:5000/).
        Displays 'C + <text>'
    """
    return "C {}".format(escape(text).replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/(<text>)", strict_slashes=False)
def python_route(text="is cool"):
    """
        Flask route at /python/<text> (http://0.0.0.0:5000/).
        Displays 'Python + <text>'
        Default value of <text> = "is cool"
    """
    return "Python {}".format(escape(text).replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
        Flask route at /number/<int:n> (http://0.0.0.0:5000/).
        Displays '<n> is a number' if <n> is an int
    """
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
        Flask route at /number_template/<int:n> (http://0.0.0.0:5000/).
        Displays 5-number.html template with value of <n>
    """
    return render_template("5-number.html", number=escape(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
