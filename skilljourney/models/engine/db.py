from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, scoped_session,sessionmaker


# Create SQLAlchemy database instance
db = SQLAlchemy()


# Define the engine for SQLAlchemy
engine = create_engine("sqlite:///app.db", echo=True)


# Create a scoped session for Flassk-SQLAlchemy
Session = scoped_session(sessionmaker(bind=engine))


# Import model classes after creating the db instance
from models.user import User
from models.post import Post
from models.comment import Comment
from models.badge import Badge
from models.achievement import Achievement
