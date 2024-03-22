from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import login_user, login_required, logout_user
from . import app
from ..models.engine import db
from .models import User
from .forms import LoginForm, RegistrationForm


auth_bp = Blueprint('auth', __name__)


# Registration page route
@auth_bp.route('/register', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Process sign_up form data
        user = User(firstname=form.firstname.data,
                    last_name=form.lastname.data,
                    username=form.username.data,
                    email=form.email.data,
                    password=form.password.data
                    )
        db.session.add(user)
        db.session.commit(user)

        # Redirect to home page after successful registration
        return redirect(url_for('home_page'))
    # If request method is GET, render the registration page template
    return render_template('sign_up.html')


# Login page route
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
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
    # Process to logout
    logout_user()
    return redirect(url_for('logout.html'))


@auth_bp.errorhandler(404)
def page_not_found(e):
    # Renders the 404.html template and returns the 404 status code
    return render_template('404.html'), 404


@auth_bp.errorhandler(500)
def internal_server_error(e):
    # Renders the 500.html template and returns the 404 status code
    return render_template('500.html'), 500
