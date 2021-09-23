from flask import Flask
from flask_bootstrap import Bootstrap
from .config import config_options
from flask_sqlalchemy import SQLAlchemy

bootstrap=Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])

    # Intializing Flask Extensions
    bootstrap.init_app(app)
    
    db.init_app(app)

    return app