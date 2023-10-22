#!/usr/bin/python3
""" This script starts a Flask application that listens on 0.0.0.0 """

from os import getenv
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
        Flask route at /cities_by_states
        Displays list of the Cities in the database with their states
    """
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
