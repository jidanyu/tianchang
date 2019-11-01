from flask import Blueprint


admin_bp = Blueprint('admin', __name__, static_folder='static', static_url_path='/admin/static')
