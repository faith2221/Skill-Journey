from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from .forms import UserProfileForm
from .models import User


user_bp = Blueprint('user', __name__)


@user_bp.route('/profile')
@login_required
def profile():
    user = current_user
    return render_template('profile.html', user=user)


@user_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    # Handle account settings form submission
    return render_template('settings.html')


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
    return redirection(url_for('profile'))


@user_bp.route('/skills/edit/<int:skill_id>', methods=['GET', 'POST'])
@login_required
def edit_skill(skill_id):
    # Logic to edit an exissting skill for current user
    return redirect(url_for('profile'))


@user_bp.route('/skills/delete/<int:skill_id>' methods=['POST'])
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


@user_bp.route('/search/skills')
@login_required
def search_skills():
    # Logic to search for skills
    return render_template('search_skills.html')
