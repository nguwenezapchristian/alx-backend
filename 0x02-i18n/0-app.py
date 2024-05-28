#!/usr/bin/env python3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Render the index.html template for the root URL.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    """
    Run the Flask application in debug mode on port 5000.
    """
    app.run(debug=True, port=5000)
