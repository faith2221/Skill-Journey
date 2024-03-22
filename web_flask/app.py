from flask import Flask, render_template
from flask import request, redirect, url_for
from .models import User
from ..models.engine import db
from auth_bp.auth import auth_bp
from user_bp.user import user_bp
from admin_bp.admin import admin_bp


app = Flask(__name__)


app.register_blueprint(auth_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)


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
