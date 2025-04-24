from flask import Flask
from api.controllers.controller_animal import animales_bp


def create_app():
    app = Flask(__name__, template_folder='views')

    app.register_blueprint(animales_bp)

    return app
