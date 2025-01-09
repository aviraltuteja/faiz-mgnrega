import os
from dotenv import load_dotenv
from flask import Flask
from flask import Flask
from iCore.app.routes.routes import blp as routesBlueprint


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['SECRET_KEY'] ="secret-key"

    
    app.register_blueprint(routesBlueprint)

    return app