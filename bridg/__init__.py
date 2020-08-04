"""Main application."""
from flask import Flask


def index():
    """Hello world function."""
    return "Hello World!"


def create_app():
    """Return an Flask app instance."""
    app = Flask(__name__)

    app.add_url_rule('/', 'index', index)

    return app
