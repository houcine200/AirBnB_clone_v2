#!/usr/bin/python3
"""
Flask web app to display list of states and cities using SQLAlchemy and Jinja.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    """Render states html page to display list of States."""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def display_state_cities(id):
    """Render state_cities html page to display State and Cities."""
    state = storage.get(State, id)
    if state:
        return render_template("9-states.html", state=state)
    else:
        return render_template("9-states.html", not_found=True)


@app.teardown_appcontext
def tear_down_db(exception):
    """Method to remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
