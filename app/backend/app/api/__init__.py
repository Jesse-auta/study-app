from flask import Blueprint

# Create a blueprint for all API routes
api_bp = Blueprint("api", __name__)

# Import routes so they attach to api_bp
# from app.api import projects
from .projects import project_bp
from .notes import notes_bp

api_bp.register_blueprint(project_bp)
api_bp.register_blueprint(notes_bp)
