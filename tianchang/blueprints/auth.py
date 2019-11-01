from flask import Blueprint


auth_bp = Blueprint('auth', __name__, static_folder='static', static_url_path='/auth/static')


# @auth_bp.route('/login')
# def login():
#

# @auth_bp.route('/logout')
# def logout()
