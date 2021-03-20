"""A module containing Flask app initialization and configuration"""

from flask import Flask
from .extensions import db
from .routes import shortener

def create_app(config_file):
    """Returns flask app """
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    db.init_app(app)
    app.register_blueprint(shortener)
    return app

app = create_app("settings.py")
