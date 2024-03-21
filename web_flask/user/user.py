from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from .forms import UserProfileForm
from .models import User


user_bp = Blueprint('user', __name__)


@user_bp.route('/profile')
@login_required
def profile():
    form = UserProfileForm()
    if form.validate_on_submit():
        # Update user profile information
        current_user.username = form.username.data
        current_user.email = form.email.data

        # Commit changes to the database
        db.session.commit()
        return redirect(url_for('user.profile'))
    return render_template('profile.html', form=form, user=user)


@user_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = UserProfileForm()
    if form.validate_on_submit():
        # Handle account settings form submission
        flash('Settings updated successfully', 'success')
        return redirect(url_for('user.settings'))
    return render_template('settings.html', form=form)


@user_bp.route('/dashboard')
@login_required
def dashboard():
    # Retrieves user_specific data for the dashboard
    return render_template('dashboard.html')


@user_bp.route('/activity')
@login_required
def activity():
    # Retrieves and display user activity history
    return render_template('activity.html')


@user_bp.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    return redirect(url_for('landing_page'))


@user_bp.route('/skills/add', methods=['GET', 'POST'])
@login_required
def add_skill():
    # Logic to add a new skill for the current user
    return redirect(url_for('profile'))


@user_bp.route('/skills/edit/<int:skill_id>', methods=['GET', 'POST'])
@login_required
def edit_skill(skill_id):
    # Logic to edit an exissting skill for current user
    return redirect(url_for('profile'))


@user_bp.route('/skills/delete/<int:skill_id>', methods=['POST'])
@login_required
def delete_skill(skill_id):
    # Logic to delete a skill for the current user
    return redirect(url_for('profile'))


@user_bp.route('//progress/update/<int:skill_id>', methods=['POST'])
@login_required
def update_progress(skill_id):
    # Logic to update progress for a skill
    return redirect(url_for('profile'))


@user_bp.route('/search/skills')
@login_required
def search_skills():
    # Logic to search for skills
    return render_template('search_skills.html')


@user_bp.route('/search/users')
@login_required
def search_users():
    # Logic to search for users
    return render_template('search_users.html')


@user_bp.errorhandler(404)
def page_not_found(e):
    # Renders the 404.html template and returns the 404 status code
    return render_template('404.html'), 404


@user_bp.errorhandler(500)
def internal_server_error(e):
    # Renders the 500.html template and returns the 404 status code
    return render_template('500.html'), 500
