#!/usr/bin/env python3
"""
Basic Babel setup implementation
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    In order to configure available languages in our app, you will create
    a Config class that has a LANGUAGES class attribute equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello() -> str:
    """
    Render the index.html template for the root URL.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    """
    Run the Flask application in debug mode on port 5000.
    """
    app.run(debug=True, port=5000)
