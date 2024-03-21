from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required
from ..forms import UserProfileForm
from ..models.post import Post
from ..models.comment import Comment
from ..models import User
from .. import db

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

        # Flash success message
        flash('Profile updated successfully', 'success')
        return redirect(url_for('user.profile'))
    
    # Prefill form with current user data
    form.username.data = current_user.username
    form.email.data = current_user.email

    return render_template('profile.html', form=form, user=current_user)


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


@user_bp.route('/posts')
@login_required
def posts():
    # Retrieves user's posts from database
    posts = current_user.posts.all()
    return render_template('posts.html', posts=posts)


@user_bp.route('/posts/create', methods=['GET', 'POST'])
@login_required
def create_post():
    # Handle post creation form submission
    return render_template('create_post.html')


@user_bp.route('/posts/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    # Retrieve the post from the database
    post = Post.query.get_or_404(post_id)

    # Handle post editing form submission
    return render_template('edit_post.html', pst=post)


@user_bp.route('/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    # Retrieve the post from the database and delete it
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully.', 'success')
    return redirect(url_for('user.posts'))


@user_bp.route('/posts/<int:post_id>/comments', methods=['POST'])
@login_required
def add_comment(post_id):
    # Handle comment form submission
    return render_template('comments.html')


@user_bp.route('/comments/<int:comment_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_comment(comment_id):
    # Retrieve the comment from the database
    comment = Comment.query.get_or_404(comment_id)

    if request.method == 'POST':
        # Handle comment editing form submission
        db.session.commit()
        flash('Comment edited successfully.', 'success')
        return redirect(url_for('user.posts'))

    # Render the edit comment form
    return render_template('edit_comment.html', comment=comment)


@user_bp.route('/comments/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    # Retrieve the comment from the database and delete it
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully.', 'success')
    return redirect(url_for('user.posts'))


@user_bp.route('/favorites')
@login_required
def favorites():
    # Retrieves user's favorite items from the database
    favorites = current_user.favorites.all()
    return render_template('favorites.html', favorites=favorites)


@user_bp.route('/favorites/add/<int:item_id>', methods=['POST'])
@login_required
def add_favorite():
    # Handle adding an item to the user's favorites
    return redirect(url_for('user.favorites'))


@user_bp.route('/favorites/remove/<int:item_id>', methods=['POST'])
@login_required
def remove_favorite():
    # Handle removing an item to the user's favorites
    return redirect(url_for('user.favorites'))


@user_bp.errorhandler(404)
def page_not_found(e):
    # Renders the 404.html template and returns the 404 status code
    return render_template('404.html'), 404


@user_bp.errorhandler(500)
def internal_server_error(e):
    # Renders the 500.html template and returns the 404 status code
    return render_template('500.html'), 500
