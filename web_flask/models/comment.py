from .engine.db import db
from .user import User
from datetime import datetime


class Comment(db.Model):
    """Model for post comments."""


    __tablename__ = 'comments'


    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False,
                          default=datetime.utcnow)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


    def __repr__(self):
        return '<Post %r>' % self.id
