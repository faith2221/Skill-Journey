from .engine.db import db
from .user import User
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Achievement(db.Model):
    """ Model for achievement."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    
    def __repr__(self):
        return '<Achievement %r>' % self.name
