from flask import Flask
from flask import render_template, redirect, url_for
from flask_migrate import Migrate
from flask import request
from models.engine.db import db
from models.user import User
from models.post import Post
from models.comment import Comment
from models.badge import Badge
from models.achievement import Achievement
from forms import RegistrationForm, LoginForm, UserProfileForm, PostForm, CommentForm
from auth_bp.auth import auth_bp
from user_bp.user import user_bp
from admin_bp.admin import admin_bp


app = Flask(__name__)


# Configure database URI
db_path = 'sqlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Intialize SQLAlchemy db instance
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)


app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)


# Ensure proper context management for database sessions
@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


# Landing page route
@app.route('/')
def landing_page():
    return render_template('landing.html')


# Home page route(after login)
@app.route('/home')
def home_page():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
