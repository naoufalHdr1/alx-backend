#!/usr/bin/env python3
"""
A basic Flask application that renders a simple HTML page.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """
    Renders the index page with a welcome message.
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(debug=True)
