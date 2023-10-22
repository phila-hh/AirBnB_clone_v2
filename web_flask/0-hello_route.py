#!/usr/bin/python3
"""
0-hello_route module
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
