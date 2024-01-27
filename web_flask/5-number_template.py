#!/usr/bin/python3
"""Starts a Flask web application with specific routes."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays "Hello HBNB!" when the root URL is accessed."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays "HBNB" when the /hbnb URL is accessed."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays 'C ' followed by text."""
    clean_text = text.replace("_", " ")
    return f"C {clean_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """Displays 'Python ' followed by text."""
    clean_text = text.replace("_", " ")
    return f"Python {clean_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """Displays 'n is a number' only if n is an integer."""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Displays an HTML page only if n is an integer."""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
