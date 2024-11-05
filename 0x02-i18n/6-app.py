#!/usr/bin/env python3
"""
Flask application with basic Babel setup for internationalization (i18n).
Supports English and French locales.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# Mock user database
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    LANGUAGES = ['en', 'fr']  # Supported languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default locale if none is specified
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone

app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Select the best locale for the user based on a prioritized order.
    
    The order of priority is:
    1. Locale from URL parameters
    2. Locale from user settings
    3. Locale from request header
    4. Default locale
    """
    # Check for a locale in the URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Check for a user's preferred locale if logged in
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    # Fallback to the best match from the request header
    return request.accept_languages.best_match(app.config['LANGUAGES']) or app.config['BABEL_DEFAULT_LOCALE']

def get_user() -> dict:
    """
    Retrieve the user based on the 'login_as' parameter in the URL.
    """
    user_id = request.args.get('login_as')
    if user_id and user_id.isdigit():
        user_id = int(user_id)
        return users.get(user_id)
    return None

@app.before_request
def before_request() -> None:
    """
    Function to be executed before each request.
    Sets the user information in the global context if available.
    """
    g.user = get_user()

@app.route('/')
def index() -> str:
    """
    Render the index page with a welcome message.
    Displays a message based on the user's login status.
    """
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run()
