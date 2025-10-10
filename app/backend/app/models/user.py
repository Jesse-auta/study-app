from app.extensions import db
from datetime import datetime, timezone
import bcrypt


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(90),unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    #Relationships
    projects = db.relationship("Project", backref="user", lazy=True)
    notes = db.relationship("Note", backref="user", lazy=True)
    resources = db.relationship("Resource", back_populates="user", cascade="all, delete-orphan")



    def set_password(self, password):
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode("UTF-8"), salt).decode("UTF-8")


    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

