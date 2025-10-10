from app.extensions import db
from datetime import datetime, timezone

class Resource(db.Model):
    __tablename__ = "resources"

    id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String(256), nullable=False)
    url = db.Column(db.String(500), nullable=False)  
    thumbnail_url = db.Column(db.String(255), nullable=True)
    resource_type = db.Column(db.String(50), nullable=False, default="video")  
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    #table relationships
    project = db.relationship("Project", back_populates="resources")
    user = db.relationship("User", back_populates="resources")