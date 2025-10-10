from datetime import datetime, timezone
from app.extensions import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(250), unique=True, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    notes = db.relationship("Note", back_populates="project", cascade="all, delete-orphan")
    resources = db.relationship("Resource", back_populates="project", cascade="all, delete-orphan")

    
    
    def to_dict(self):
        """Convert model object into a dictionary for JSON responses."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
        

