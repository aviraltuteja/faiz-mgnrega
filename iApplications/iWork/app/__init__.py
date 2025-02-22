import os
from flask import Flask
from flask import redirect, url_for
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_migrate import Migrate
from iWork.app.db import db
from iWork.app.models import User
from iWork.app.routes.routes import blp as routeBlueprint
from iWork.app.routes.auth import blp as authBlueprint
from iWork.app.routes.admin import blp as adminBlueprint

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://faiz_mgnrega_user:2cVrCcMdQLRADukcpHO5i0K8s2KUMbN4@dpg-cupa45ggph6c73dtiqig-a.oregon-postgres.render.com/faiz_mgnrega"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']="WORK_SECRET_KEY"

    db.init_app(app)
    current_directory = os.getcwd()
    migrations_directory = current_directory + '/iWork/migrations'
    migrate = Migrate(app, db, directory=migrations_directory)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    jwt = JWTManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(routeBlueprint)
    app.register_blueprint(authBlueprint)
    app.register_blueprint(adminBlueprint)

    # Default route to redirect to register page


    return app