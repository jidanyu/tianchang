import os

from flask import render_template, flash, redirect, url_for, request, current_app, Blueprint, send_from_directory
from flask_login import login_required, current_user
from flask_ckeditor import upload_success, upload_fail

from tianchang.extensions import db
from tianchang.forms import SettingForm, PostForm, CategoryForm, LinkForm
from tianchang.models import Post, Category, Comment, Link
from tianchang.utils import redirect_back, allowed_file

admin_bp = Blueprint('admin', __name__, static_folder='static', static_url_path='/admin/static')


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


@admin_bp.route('/post/manage')
@login_required
def manage_post():
    return '这是设置界面'


@admin_bp.route('/category/manage')
@login_required
def manage_category():
    return '这是设置界面'


@admin_bp.route('/comment/manage')
@login_required
def manage_comment():
    return '这是设置界面'


@admin_bp.route('/link/manage')
@login_required
def manage_link():
    return '这是设置界面'


@admin_bp.route('/new_category')
@login_required
def new_category():
    return '这是设置界面'


@admin_bp.route('/new_link')
@login_required
def new_link():
    return '这是设置界面'


@admin_bp.route('/set_commemt')
@login_required
def set_commemt():
    return '这是设置界面'


@admin_bp.route('/setting')
@login_required
def settings():
    return '这是设置界面'
