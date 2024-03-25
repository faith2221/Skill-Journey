from flask import Blueprint, redirect, url_for, render_template
from flask import request
from flask_login import login_user, login_required, logout_user
from . import app
from skilljourney.models.engine.db import db
from skilljourney.models.user import User
from skilljourney.models.badge import Badge
from skilljourney.models.achievement import Achievement
from .forms import LoginForm, RegistrationForm


auth_bp = Blueprint('auth', __name__)


# Function to generate a random strong password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation)
    return ''.join(choice(characters) for _ in range(length))


#Route to generate and suggest a strong password
@auth_bp.route('/suggest_password')
def logout():
    """ Process to generate password."""
    password = generate_random_password()
    return render_template('suggest_password.html', password=password)


# Registration page route
@auth_bp.route('/register', methods=['GET', 'POST'])
def sign_up():
    """ Initialize the registration form."""
    form = RegistrationForm()
    if form.validate_on_submit():
        # Process sign_up form data
        user = User(firstname=form.firstname.data,
                    last_name=form.lastname.data,
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                    )
        db.session.add(user)
        db.session.commit()

        # Redirect to home page after successful registration
        return redirect(url_for('home_page'))
    # If request method is GET, render the registration page template
    return render_template('sign_up.html')


# Login page route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ Logic for login."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        # Redirect to home page after successful login
        return redirect(url_for('home_page'))
    # If request method is GET, render the login page template
    return render_template('login.html', form=form)


# Logout page route
@auth_bp.route('/logout')
@login_required
def logout():
    """ Process to logout."""
    logout_user()
    return redirect(url_for('home_page'))


@auth_bp.errorhandler(404)
def page_not_found(e):
    """ Renders the 404.html template and returns the 404 status code."""
    return render_template('404.html'), 404


@auth_bp.errorhandler(500)
def internal_server_error(e):
    """ Renders the 500.html template and returns the 500 status code."""
    return render_template('500.html'), 500
