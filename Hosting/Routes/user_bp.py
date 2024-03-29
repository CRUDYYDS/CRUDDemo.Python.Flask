from flask import Blueprint

from Hosting.Controllers.UserController import add, get, update, delete

user_bp = Blueprint('user_bp', __name__)


user_bp.route('/add', methods=['POST'])(add)
user_bp.route('/<int:userId>', methods=['GET'])(get)
user_bp.route('/update', methods=['POST'])(update)
user_bp.route('/delete/<int:userId>', methods=['GET'])(delete)
