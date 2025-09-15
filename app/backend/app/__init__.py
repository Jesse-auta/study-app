from flask import Flask
from app.extensions import db, migrate, cors
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from app.config import Config
import os

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # register blueprints
    from app.api import api_bp
    app.register_blueprint(api_bp)
    # app.register_blueprint()
    return app
