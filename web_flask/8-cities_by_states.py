#!/usr/bin/python3
"""A Flask Web App that renders a page with states and cities"""

from flask import Flask, render_template
from models import storage
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.state import State

app = Flask(__name__)
states = storage.all(State)
states_cities_map = {}

for state in states.values():
    if isinstance(storage, DBStorage):
        state_cities = State.cities.__get__(state, State)
    elif isinstance(storage, FileStorage):
        state_cities = state.cities()

    states_cities_map[state] = state_cities


@app.route("/cities_by_states", strict_slashes=False)
def display_states():
    """Displays states"""
    return render_template("8-cities_by_states.html",
                           st=states, st_ct_map=states_cities_map)


@app.teardown_appcontext
def remove_sqlsession(exception=None):
    """A method that removes SQL Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
