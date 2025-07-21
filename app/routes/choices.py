from flask import Blueprint, request, jsonify
from config import db
from app.models import Choice

choices_bp = Blueprint('choices', __name__)

@choices_bp.route('/', methods=['POST'])
def create_choice():
    data = request.get_json()
    new_choice = Choice(question_id=data['question_id'], choice_text=data['choice_text'])
    db.session.add(new_choice)
    db.session.commit()
    return jsonify({'message': 'Choice created successfully!'}), 201

@choices_bp.route('/', methods=['GET'])
def get_choices():
    choices = Choice.query.all()
    return jsonify([choice.to_dict() for choice in choices])

@choices_bp.route('/<int:id>', methods=['GET'])
def get_choice(id):
    choice = Choice.query.get_or_404(id)
    return jsonify(choice.to_dict())

@choices_bp.route('/<int:id>', methods=['PUT'])
def update_choice(id):
    choice = Choice.query.get_or_404(id)
    data = request.get_json()
    choice.question_id = data['question_id']
    choice.choice_text = data['choice_text']
    db.session.commit()
    return jsonify({'message': 'Choice updated successfully!'})

@choices_bp.route('/<int:id>', methods=['DELETE'])
def delete_choice(id):
    choice = Choice.query.get_or_404(id)
    db.session.delete(choice)
    db.session.commit()
    return jsonify({'message': 'Choice deleted successfully!'})
