from .engine.db import db
from .user import User
from datetime import datetime


user_badge = db.Table(
        'user_badge',
        db.Column('user_id', db.Integer, db.ForeignKey('user_id'),
                  primary_key=True),
        db.Column('badge_id', db.Integer, db.ForeignKey('badge.id'),
                  primary_key=True)


class Badge(db.Model):
    """ Model for badges."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        return '<Badge %r>' % self.name
