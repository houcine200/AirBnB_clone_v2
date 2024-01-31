#!/usr/bin/python3
"""
Flask web app to display list of states and cities using SQLAlchemy and Jinja.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities_by_states():
    """Render cities_by_states html page to display States and Cities."""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def tear_down_db(exception):
    """Method to remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
