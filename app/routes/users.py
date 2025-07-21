from flask import Blueprint, request, jsonify
from config import db
from app.models import User

user_blp = Blueprint('users', __name__, url_prefix='/users')

@user_blp.route('/', methods=['POST'], strict_slashes=False)
def create_user():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'message': 'Request must contain JSON data'}), 400

        # 필수 필드 확인
        required_fields = ['name', 'age', 'gender', 'email']
        for field in required_fields:
            if field not in data:
                return jsonify({'message': f'Missing required field: {field}'}), 400

        new_user = User(
            name=data['name'], 
            age=data['age'],
            gender=data['gender'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'user_id': new_user.id}), 201
    except KeyError as e:
        return jsonify({'message': f'Invalid data provided: Missing key {e}'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': f'An error occurred: {str(e)}'}), 500

@user_blp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_blp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@user_blp.route('/<int:id>', methods=['PUT'], strict_slashes=False)
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data['name']
    user.age = data['age']
    user.gender = data['gender']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@user_blp.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})