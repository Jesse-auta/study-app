from app.extensions import db
from datetime import datetime, timezone, timedelta

class Timer(db.Model):
    __tablename__ = "timers"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    end_time = db.Column(db.DateTime, nullable=True)

    # Whether the timer is active or finished
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, user_id, project_id, duration_seconds):
        self.user_id = user_id
        self.project_id = project_id
        self.duration_seconds = duration_seconds
        self.start_time = datetime.now(timezone.utc)
        self.end_time = self.start_time + timedelta(seconds=duration_seconds)
        self.is_active = True

        if duration_seconds is not None:
            self.end_time = self.start_time + timedelta(seconds=duration_seconds)
        else:
            self.end_time = None