from flask import Blueprint, request, jsonify
from config import db
from app.models import Choice

choices_blp = Blueprint('choices', __name__, url_prefix='/choices')

@choices_blp.route('/', methods=['POST'])
def create_choice():
    data = request.get_json()
    new_choice = Choice(
        question_id=data['question_id'], 
        content=data['content'],
        sqe=data['sqe'],
        is_active=data.get('is_active', True)
    )
    db.session.add(new_choice)
    db.session.commit()
    return jsonify({'message': 'Choice created successfully!'}), 201

@choices_blp.route('/', methods=['GET'])
def get_choices():
    choices = Choice.query.all()
    return jsonify([choice.to_dict() for choice in choices])

@choices_blp.route('/<int:id>', methods=['GET'])
def get_choice(id):
    choice = Choice.query.get_or_404(id)
    return jsonify(choice.to_dict())

@choices_blp.route('/<int:id>', methods=['PUT'])
def update_choice(id):
    choice = Choice.query.get_or_404(id)
    data = request.get_json()
    choice.question_id = data['question_id']
    choice.content = data['content']
    choice.sqe = data['sqe']
    choice.is_active = data.get('is_active', choice.is_active)
    db.session.commit()
    return jsonify({'message': 'Choice updated successfully!'})

@choices_blp.route('/<int:id>', methods=['DELETE'])
def delete_choice(id):
    choice = Choice.query.get_or_404(id)
    db.session.delete(choice)
    db.session.commit()
    return jsonify({'message': 'Choice deleted successfully!'})