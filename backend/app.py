from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from configuration import app_config
from routes import configure_routes
from db import db
import logging


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    CORS(app)
    api = Api(app)
    configure_routes(api)
    db.init_app(app)
    logging.basicConfig(level=logging.INFO)
    return app
