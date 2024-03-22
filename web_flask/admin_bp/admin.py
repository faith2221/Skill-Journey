from flask import Blueprint, render_template, redirect, url_for, flash
from flask import request
from flask_login import current_user, login_required
from ..models.engine import db
from .models import User, Post, Comment
from .forms import UserProfileForm, PostForm, CommentForm


admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # Dashboard for admin tasks
    return render_template('admin/dashboard.html')


@admin_bp.route('/admin/users')
@login_required
def manage_users():
    # User management page
    users = User.query.all()
    return render_template('admin/manage_users.html', user=user)


@admin_bp.route('/admin/users/<int:user_id>', methods=['GET', 'POST'])
@login_required
def edit_user(user_id):
    # Edit user profile page
    user = User.query.get_or_404(user_id)
    form = UserProfileForm(obj=user)
    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()

        flash('User profile updated successfully.', 'success')
        return redirect(url_for('admin.manage_users'))
    return render_template('admin/edit_user.html', form=form, user=user)


@admin_bp.route('/admin/posts')
@login_required
def manage_posts():
    # Post management page
    posts = Post.query.all()
    return render_template('admin/manage_posts.html', posts=posts)


@admin_bp.route('/admin/posts/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    # Edit post page
    post = Post.query.get_or_404(post_id)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        form.populate_obj(post)
        db.session.commit()

        flash('Post updated successfully.', 'success')
        return redirect(url_for('admin.manage_posts'))
    return render_template('admin/edit_post.html', form=form, post=post)


@admin_bp.route('/admin/posts/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    # Delete post
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully.', 'success')
    return redirect(url_for('admin.manage_posts'))


@admin_bp.route('/admin/comments')
@login_required
def manage_comments():
    # Comment management page
    comments = Comment.query.all()
    return render_template('admin/manage_comments.html', comments=comments)


@admin_bp.route('/admin/comments/<int:comment_id>', methods=['GET', 'POST'])
@login_required
def edit_comment(comment_id):
    # Edit comment page
    comment = Comment.query.get_or_404(comment_id)
    form = CommentForm(obj=comment)
    if form.validate_on_submit():
        form.populate_obj(comment)
        db.session.commit()

        flash('Comment updated successfully.', 'success')
        return redirect(url_for('admin.manage_comments'))
    return render_template('admin/edit_comment.html', form=form, comment=comment)


@admin_bp.route('/admin/comments/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    # Delete comment
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted successfully.', 'success')
    return redirect(url_for('admin.manage_comments'))


@admin_bp.route('/admin/settings', methods=['GET', 'POST'])
@login_required
def admin_settings():
    # Settings management page
    if request.method == 'POST':
        # Handle form submission
        flash('Settings updated successfully.', 'success')
        return redirect(url_for('admin.admin_settings'))
    return render


@admin_bp.route('/admin/analytics')
@login_required
def view_analytics():
    # Analytics and reporting page
    return render_template('admin/analytics.html')


@admin_bp.route('/admin/backups')
@login_required
def manage_backups():
    # Database backups management page
    return render_template('admin/manage_backups.html')


@admin_bp.route('/admin/system')
@login_required
def system_management():
    # System administration page
    return render_template('admin/system_management.html')


@admin_bp.errorhandler(404)
def page_not_found(e):
    # Renders the 404.html template and returns the 404 status code
    return render_template('404.html'), 404


@admin_bp.errorhandler(500)
def internal_server_error(e):
    # Renders the 500.html template and returns the 500 status code
    return render_template('500.html'), 500
