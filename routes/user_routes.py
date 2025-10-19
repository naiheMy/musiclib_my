from flask import Blueprint, request
from sqlite3 import IntegrityError
from models import db, User
from utils.response_util import make_response  # 修改导入路径

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/add', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    gender = data.get('gender', 0)  # 默认值0
    age = data.get('age')
    avatar = data.get('avatar', '')  # 默认值空字符串
    
    if not username or not email or not password:
        return make_response(400, None, '缺少用户名、邮箱或密码')

    # 验证age是否为有效数字
    if age is not None and age != '':
        try:
            age = int(age)
        except ValueError:
            return make_response(400, None, '年龄必须是有效数字')
    else:
        age = None  # 或者设置为默认值如0

    # 同时检查用户名和邮箱是否已存在
    existing_user = User.query.filter(
        (User.username == username) | (User.email == email)
    ).first()
    
    if existing_user:
        if existing_user.username == username:
            return make_response(400, None, '用户名已存在')
        else:
            return make_response(400, None, '邮箱已存在')

    new_user = User(
        username=username,
        email=email,
        password=password,
        gender=gender,
        age=age,  # 使用处理后的age值
        avatar=avatar
    )
    db.session.add(new_user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return make_response(400, None, '插入失败，用户名或邮箱重复')
    except Exception as e:
        db.session.rollback()
        return make_response(500, None, f'数据库错误: {str(e)}')

    return make_response(200, {'id': new_user.id}, '用户注册成功')

@user_bp.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return make_response(400, None, '缺少必要参数（邮箱/密码）')

    user = User.query.filter_by(email=email).first()
    if not user:
        return make_response(404, None, '用户不存在')

    if user.password != password:
        return make_response(401, None, '密码错误')

    return make_response(200, {'id': user.id}, '登录成功')

@user_bp.route('/delete/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return make_response(404, None, '用户不存在')

    try:
        db.session.delete(user)
        db.session.commit()
        return make_response(200, None, '用户删除成功')
    except Exception as e:
        db.session.rollback()
        return make_response(500, None, f'删除用户失败: {str(e)}')

@user_bp.route('/update/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return make_response(404, None, '用户不存在')

    data = request.get_json()
    new_username = data.get('username')
    new_email = data.get('email')

    if new_username:
        user.username = new_username
    if new_email:
        existing_user = User.query.filter_by(email=new_email).first()
        if existing_user and existing_user.id != user_id:
            return make_response(400, None, '邮箱已存在，无法更新用户信息')
        user.email = new_email

    try:
        db.session.commit()
        return make_response(200, {'id': user.id}, '用户更新成功')
    except IntegrityError:
        db.session.rollback()
        return make_response(400, None, '更新失败，可能是用户名或邮箱重复')
    except Exception as e:
        db.session.rollback()
        return make_response(500, None, f'数据库错误: {str(e)}')

@user_bp.route('/all', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        user_list = [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'gender': user.gender,
            'age': user.age,
            'avatar': user.avatar
        } for user in users]
        return make_response(200, user_list, '获取用户列表成功')
    except Exception as e:
        return make_response(500, None, f'获取用户列表失败: {str(e)}')