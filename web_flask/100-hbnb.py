#!/usr/bin/python3
"""Web App with Flask"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def display_page():
    """Display the HBNB page"""
    list_states = storage.all(State)
    list_amenity = storage.all(Amenity)
    return render_template("100-hbnb.html", states=list_states,
                           amenities=list_amenity)


@app.teardown_appcontext
def remove_sqlsession(exception=None):
    """A method that removes SQL Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
