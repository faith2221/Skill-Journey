from .engine.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    """Model for user accounts."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)


    def __repr__(self):
        return '<User %r>' % self.username


    def set_password(self, password):
        """ Set the user's password."""
        self.password_hash = hash_password(password)


    def check_password(self, password):
        """Check if the provided password matches the user's password."""
        return verify_password(self.password_hash, password)
