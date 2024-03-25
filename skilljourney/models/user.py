from .engine.db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(db.Model, UserMixin):
    """Model for user accounts."""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(100), nullable=False)

    posts = db.relationship('Post', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    badges = db.relationship('Badge', secondary='user_badge', backref='users')
    achievements = db.relationship('Achievement', backref='user', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', {self.image_file}')"


    def set_password(self, password):
        """ Set the user's password."""
        self.password_hash = hash_password(password)


    def check_password(self, password):
        """Check if the provided password matches the user's password."""
        return verify_password(self.password_hash, password)
