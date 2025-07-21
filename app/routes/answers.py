from flask import Blueprint, request, jsonify
from config import db
from app.models import Answer

answers_blp = Blueprint('answers', __name__, url_prefix='/answers')

@answers_blp.route('/', methods=['POST'])
def create_answer():
    data = request.get_json()
    required_fields = ['user_id', 'question_id', 'choice_id']
    for field in required_fields:
        if field not in data:
            return jsonify({'message': f'Missing required field: {field}'}), 400

    new_answer = Answer(
        user_id=data['user_id'],
        question_id=data['question_id'],
        choice_id=data['choice_id']
    )
    db.session.add(new_answer)
    db.session.commit()
    return jsonify({'message': 'Answer created successfully!'}), 201

@answers_blp.route('/', methods=['GET'])
def get_answers():
    answers = Answer.query.all()
    return jsonify([answer.to_dict() for answer in answers])

@answers_blp.route('/<int:id>', methods=['GET'], strict_slashes=False)
def get_answer(id):
    answer = Answer.query.get_or_404(id)
    return jsonify(answer.to_dict())

@answers_blp.route('/<int:id>', methods=['PUT'], strict_slashes=False)
def update_answer(id):
    answer = Answer.query.get_or_404(id)
    data = request.get_json()
    answer.user_id = data['user_id']
    answer.choice_id = data['choice_id']
    db.session.commit()
    return jsonify({'message': 'Answer updated successfully!'})

@answers_blp.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_answer(id):
    answer = Answer.query.get_or_404(id)
    db.session.delete(answer)
    db.session.commit()
    return jsonify({'message': 'Answer deleted successfully!'})