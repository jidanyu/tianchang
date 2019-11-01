from flask import Blueprint


blog_bp = Blueprint('blog', __name__, static_folder='static', static_url_path='/blog/static')


@blog_bp.route('/')
def index():
    return 'Helllo jidanyu'
