#!/usr/bin/env python3
"""
Basic Babel setup implementation.
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

class Config:
    """
    Configuration class for Flask application.
    Contains language and timezone settings.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

""" Check if the Babel object has the localeselector method """
if hasattr(babel, 'localeselector'):
    @babel.localeselector
    def get_locale() -> str:
        """
        Get the best match locale from the request.

        Returns:
            str: Best match language.
        """
        return request.accept_languages.best_match(app.config['LANGUAGES'])
else:
    """ Fallback to setting the locale selector function manually """
    def get_locale() -> str:
        """
        Get the best match locale from the request.

        Returns:
            str: Best match language.
        """
        return request.accept_languages.best_match(app.config['LANGUAGES'])

    babel.localeselector_func = get_locale

@app.route('/', strict_slashes=False)
def hello() -> str:
    """
    Render the 2-index.html template for the root URL.

    Returns:
        str: Rendered HTML of the 2-index.html template.
    """
    return render_template("2-index.html")

if __name__ == "__main__":
    """
    Run the Flask application in debug mode on port 5000.
    """
    app.run(debug=True, port=5000)
