from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from app.extensions import db



class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable= False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    project = db.relationship("Project", back_populates="notes")
    
    

    def to_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "content": self.content,
            "created_at": self.created_at.isoformat()
        }
    
