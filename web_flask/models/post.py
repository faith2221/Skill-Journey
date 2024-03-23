from .engine.db import db
from .user import User
from datetime import datetime


class Post(db.Model):
    """Model for user posts."""


    __tablename__ = 'posts'


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    comments = db.relationship('Comment', backref='post', lazy=True)


    def __repr__(self):
        return '<Post %r>' % self.title
