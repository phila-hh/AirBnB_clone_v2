#!/usr/bin/python3
"""
1-hbnb_route module
This module contains a script to start the flask web application
"""


from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
