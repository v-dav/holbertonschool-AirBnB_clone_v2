#!/usr/bin/python3
"""A Flask Web App that renders a page with states and cities"""

from flask import Flask, render_template
from models import storage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City

app = Flask(__name__)
states = storage.all(State)
cities = storage.all(City)


@app.route("/cities_by_states", strict_slashes=False)
def display_states():
    """Displays states"""
    return render_template("8-cities_by_states.html",
                           st=states, cities=cities)


@app.teardown_appcontext
def remove_sqlsession(exception=None):
    """A method that removes SQL Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
