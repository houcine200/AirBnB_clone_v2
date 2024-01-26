#!/usr/bin/python3
"""Starts a Flask web application with specific routes."""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!" when the root URL is accessed."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays "HBNB" when the /hbnb URL is accessed."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=0)
def c_route(text):
    """Displays "C " followed by the value of the text variable."""
    clean_text = text.replace("_", " ")
    return f"C {clean_text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
