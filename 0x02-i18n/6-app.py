#!/usr/bin/env python3
"""
Basic Babel setup implementation with user login emulation
"""
from typing import Optional
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

""" Mock user database """
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


def get_user() -> Optional[dict]:
    """Get user from login_as parameter"""
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@babel.localeselector
def get_locale() -> str:
    """Get locale from request"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    user = getattr(g, 'user', None)
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.before_request
def before_request():
    """Set user information on flask.g"""
    g.user = get_user()


@app.route('/', strict_slashes=False)
def hello() -> str:
    """
    Render the index.html template for the root URL.

    Returns:
        str: Rendered HTML of the index.html template.
    """
    return render_template("6-index.html")


if __name__ == "__main__":
    """
    Run the Flask application in debug mode on port 5000.
    """
    app.run(debug=True, port=5000)
