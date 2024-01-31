#!/usr/bin/python3
"""
Flask web app to display list of states and cities using SQLAlchemy and Jinja.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """display the states and cities list ordered by alphabet"""
    states = storage.all(State)
    if state_id:
        state_id = f"State.{state_id}"
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def tear_down_db(exception):
    """Method to remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
