from flask_wtf import Flaskform
from wtfforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DtaRequired, Email, Length, EqualTo


# Registration Form Class
class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(min=4, max=20)])
    email = StringField('First Name', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
                                                     Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                     EqualTo('password'])
    submit = SubmitField('Sign Up')


    def validate_username(self, username):
    """ Validates the username whether it's already taken or not."""
    user = User.query.filter_by(username=username.data).first()
    if user:
        raise ValidationError('This username is already taken.
                              Please choose a different one.')

    def validate_password(self, password):
    """ Validates the username whether it's already taken or not."""
    user = User.query.filter_by(password=password.data).first()
    if user:
        raise ValidationError('This password is already taken.
                              Please choose a different one.')

    def validate_password_strength(self, password):
    """ Validates the strength of the password."""
    patthern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)
                (?=.*[@$!%*?&])[A-Za-z\d@$!%*?*]{8,}$'
    if not re.match(pattern, password.data):
        raise ValidationError('Password must be atleast 8 characters long,
                              and include atleast one uppercase letter,
                              one lowercase letter,
                              one digit, and one special character.')



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
                                                   Length(min=4, max=20)])
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
