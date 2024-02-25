from flask import Blueprint, jsonify
from database.user.dao import UserDao
from flask import request

blueprint = Blueprint('users', __name__, url_prefix="/users")


#                             USER BASIC

@blueprint.route('', methods=['GET'])
def get_all_users():
    try:
        dao = UserDao()
        return jsonify(dao.get_all_users())
    except Exception as e:
        # Manejo de errores
        print(e)
        return jsonify({'error': e}), 500