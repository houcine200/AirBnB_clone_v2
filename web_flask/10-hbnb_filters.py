#!/usr/bin/python3
"""
Flask web app to display list of states and cities using SQLAlchemy and Jinja.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def show_hbnb_filters():
    """ Shows states id """
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def tear_down_db(exception):
    """Method to remove current SQLAlchemy Session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
