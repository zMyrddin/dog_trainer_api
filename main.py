from flask import Flask
import os
from init import db, ma, bcrypt, jwt
from controllers.cli_controller import db_commands
from controllers.auth_controller_register import auth_register_bp
from controllers.auth_controller_login import auth_login_bp
from controllers.customer_controller import customer_bp
from controllers.dog_controller import dog_bp
from controllers.trainer_controller import trainer_bp


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"]=os.environ.get("DATABASE_URL")
    app.config["JWT_SECRET_KEY"]=os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(db_commands)
    app.register_blueprint(auth_register_bp)
    app.register_blueprint(auth_login_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(dog_bp)
    app.register_blueprint(trainer_bp)

    return app