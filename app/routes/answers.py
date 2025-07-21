from flask import Blueprint, request, jsonify
from app import db
from app.models import Answer

answers_bp = Blueprint('answers', __name__)

@answers_bp.route('/', methods=['POST'])
def create_answer():
    data = request.get_json()
    new_answer = Answer(user_id=data['user_id'], question_id=data['question_id'], choice_id=data['choice_id'])
    db.session.add(new_answer)
    db.session.commit()
    return jsonify({'message': 'Answer created successfully!'}), 201

@answers_bp.route('/', methods=['GET'])
def get_answers():
    answers = Answer.query.all()
    return jsonify([answer.to_dict() for answer in answers])

@answers_bp.route('/<int:id>', methods=['GET'])
def get_answer(id):
    answer = Answer.query.get_or_404(id)
    return jsonify(answer.to_dict())

@answers_bp.route('/<int:id>', methods=['PUT'])
def update_answer(id):
    answer = Answer.query.get_or_404(id)
    data = request.get_json()
    answer.user_id = data['user_id']
    answer.question_id = data['question_id']
    answer.choice_id = data['choice_id']
    db.session.commit()
    return jsonify({'message': 'Answer updated successfully!'})

@answers_bp.route('/<int:id>', methods=['DELETE'])
def delete_answer(id):
    answer = Answer.query.get_or_404(id)
    db.session.delete(answer)
    db.session.commit()
    return jsonify({'message': 'Answer deleted successfully!'})
