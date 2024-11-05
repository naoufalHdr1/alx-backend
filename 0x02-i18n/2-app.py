#!/usr/bin/env python3
"""
Flask application with basic Babel setup for internationalization (i18n).
Supports English and French locales.
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Configuration class for Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on the
    Accept-Language headers in the incoming request.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """
    Renders the index page with a welcome message.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
