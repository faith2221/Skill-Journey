from flask import Flask, render_template
from flask import request, redirect, url_for
from .models import User
from .forms import LoginForm, RegistrationForm
from . import app, db

app = Flask(__name__)


# Landing page route
@app.route('/')
def landing_page():
    return render_template('landing.html')


# Home page route(after login)
@app.route('/home')
def home_page():
    return render_template('home.html')


# Registration page route
@app.route('/register', methods=['GET', 'POST'])
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
@app.route('/login', method=['GET', 'POST'])
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
@app.route('/logout')
@login_required
def logout():
    # Process to logout
    logout_user()
    return redirect(url_for('logout.html'))


if __name__ == '__main__':
    app.run(debug=True)
