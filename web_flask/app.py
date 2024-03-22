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


if __name__ == '__main__':
    app.run(debug=True)
