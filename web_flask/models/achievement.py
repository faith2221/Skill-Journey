from .engine.db import db
from .user import User
from datetime import datetime


class Achievement(db.Model):
    """ Model for achievement."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Colum(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    badges = db.relationship('Badge', secondary=user_badge,
                             backref=db.backref('achievements', lazy='dynamic'
                                 ))

    
    def __repr__(self):
        return '<Achievement %r>' % self.name
