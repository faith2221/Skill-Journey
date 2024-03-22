from flask_wtf import Flaskform
from wtfforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DtaRequired, Email, Length


# Registration Form Class
class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=8, max=15)])
    email = StringField('First Name', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired()])
    submit = SubmitField('Sign Up')


# Login Form Class
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


# UserProfile Form Class
class UserProfileForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=8, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Profile')


#Post Form Class
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update Post')
    edit = SubmitField('Edit')
    delete = SubmitField('Delete')


# Comment Form Class
class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Update Comment')
    edit = SubmitField('Edit')
    delete = SubmitField('Delete')
