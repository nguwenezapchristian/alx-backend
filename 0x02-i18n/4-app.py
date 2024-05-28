#!/usr/bin/env python3
"""
Basic Babel setup implementation
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """
    In order to configure available languages in our app, you will create
    a Config class that has a LANGUAGES class attribute equal to ["en", "fr"]
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def hello() -> str:
    """
    Render the index.html template for the root URL.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template("4-index.html")


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request """
    if 'locale' in request.args:
        """ get the value of the 'locale' argument """
        locale = request.args.get('locale')
        """check if the provided locale is supported """
        if locale in app.config['LANGUAGES']:
            return locale
    """if not supported use the default """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    """
    Run the Flask application in debug mode on port 5000.
    """
    app.run()
