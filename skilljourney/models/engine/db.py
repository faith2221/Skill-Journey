from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy database instance
db = SQLAlchemy()


# Import model classes after creating the db instance
from models.user import User
from models.post import Post
from models.comment import Comment
from models.badge import Badge
from models.achievement import Achievement
