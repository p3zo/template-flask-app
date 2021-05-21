import logging
import os
from configparser import ConfigParser

from flask import Flask
from flask_cors import CORS

__version__ = "0.1.0"

config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.ini")
config = ConfigParser()
config.read(config_file)

APP_NAME = config.get("app", "NAME")

SECRET_STRING = os.environ.get("SECRET_STRING")

logging.basicConfig()
logger = logging.getLogger("template")
logger.setLevel(logging.DEBUG)


def create_app(test_config=None):

    app = Flask(__name__)
    app.title = APP_NAME

    with app.app_context():
        from .routes import bp

        app.register_blueprint(bp)

    CORS(app)

    return app
