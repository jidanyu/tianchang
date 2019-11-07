import os

from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, send_from_directory
from flask_login import login_required, current_user
from flask_ckeditor import upload_success, upload_fail
from tianchang.extensions import db
from tianchang.forms import SettingForm, PostForm, CategoryForm, LinkForm
from tianchang.models import Post, Category, Comment, Link
from tianchang.utils import redirect_back, allowed_file


admin_bp = Blueprint('admin', __name__, static_folder='static', static_url_path='/admin/static')


@admin_bp.route('/post/manage')
@login_required
def manage_post():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, per_page=current_app.config['BLUELOG_MANAGE_POST_PER_PAGE'])
    posts = pagination.items
    return render_template('admin/manage_post.html', pagination=pagination, posts=posts, page=page)


@admin_bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('文章删除.', 'success')
    return redirect_back()


@admin_bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    form = PostForm(title=post.title, category=post.category_id, body=post.body)

    if form.validate_on_submit():
        category = Category.query.get(form.category.data)
        post.title = form.title.data
        post.body = form.body.data
        post.category = category

        db.session.commit()
        flash('文章更新.', 'success')
        return redirect(url_for('blog.show_post', post_id=post.id))
    return render_template('admin/edit_post.html', form=form)


@admin_bp.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = Category.query.get(form.category.data)
        post = Post(title=title, body=body, category=category)
        # same with:
        # category_id = form.category.data
        # post = Post(title=title, body=body, category_id=category_id)
        db.session.add(post)
        db.session.commit()
        flash('Post created.', 'success')
        return redirect(url_for('blog.show_post', post_id=post.id))
    return render_template('admin/new_post.html', form=form)


@admin_bp.route('/category/manage')
@login_required
def manage_category():
    return '这是设置界面'


@admin_bp.route('/link/manage')
@login_required
def manage_link():
    return '这是设置界面'


@admin_bp.route('/category/new')
@login_required
def new_category():
    return '这是设置界面'


@admin_bp.route('/link/new')
@login_required
def new_link():
    return '这是设置界面'


@admin_bp.route('/commemt/set')
@login_required
def set_comment():
    return '这是设置界面'


@admin_bp.route('/comment/manage')
@login_required
def manage_comment():
    return '这是设置界面'


@admin_bp.route('/comment/<int:comment_id>/delete', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    db.session.delete(comment)
    db.session.commit()
    flash('Comment deleted.', 'success')
    return redirect_back()


@admin_bp.route('/setting')
@login_required
def settings():
    return '这是设置界面'
