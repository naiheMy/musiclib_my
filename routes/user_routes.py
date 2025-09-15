from flask import Blueprint, request
from sqlite3 import IntegrityError
from models import db, User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return '缺少用户名或邮箱地址', 400

    # 检查 email 是否已存在
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return '邮箱已存在，无法添加用户', 400

    new_user = User(username=username, email=email)
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return '插入失败，可能是用户名或邮箱重复', 400
    except Exception as e:
        db.session.rollback()
        return f'数据库错误: {str(e)}', 500

    return '用户添加成功'

@user_bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return '用户不存在', 404

    db.session.delete(user)
    db.session.commit()
    return '用户删除成功'

@user_bp.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return '用户不存在', 404

    data = request.get_json()
    new_username = data.get('username')
    new_email = data.get('email')

    # 更新用户名和邮箱
    if new_username:
        user.username = new_username
    if new_email:
        existing_user = User.query.filter_by(email=new_email).first()
        if existing_user and existing_user.id != user_id:
            return '邮箱已存在，无法更新用户信息', 400
        user.email = new_email

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return '更新失败，可能是用户名或邮箱重复', 400
    except Exception as e:
        db.session.rollback()
        return f'数据库错误: {str(e)}', 500

    return '用户更新成功'

@user_bp.route('/all', methods=['GET'])
def get_users():
    users = User.query.all()
    return '<br>'.join([f'{user.username} ({user.email})' for user in users])