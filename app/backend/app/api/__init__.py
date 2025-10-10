from flask import Blueprint

# Create a blueprint for all API routes
api_bp = Blueprint("api", __name__)

# Import routes so they attach to api_bp
# from app.api import projects
from .projects import project_bp
from .notes import notes_bp
from .users import users_bp
from .timers import timers_bp
from .resources import resources_bp

api_bp.register_blueprint(project_bp)
api_bp.register_blueprint(notes_bp)
api_bp.register_blueprint(users_bp)
api_bp.register_blueprint(timers_bp)
api_bp.register_blueprint(resources_bp)
