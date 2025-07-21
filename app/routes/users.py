from flask import Blueprint, request, jsonify
from config import db
from app.models import User

user_blp = Blueprint('users', __name__, url_prefix='/users')

@user_blp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name=data['name'], 
        age=data['age'],
        gender=data['gender'],
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'}), 201

@user_blp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@user_blp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@user_blp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()
    user.name = data['name']
    user.age = data['age']
    user.gender = data['gender']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@user_blp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully!'})