from flask import Blueprint, request, jsonify
from app import db
from app.models import Question

questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()
    new_question = Question(question_text=data['question_text'])
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Question created successfully!'}), 201

@questions_bp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return jsonify([question.to_dict() for question in questions])

@questions_bp.route('/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get_or_404(id)
    return jsonify(question.to_dict())

@questions_bp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    question = Question.query.get_or_404(id)
    data = request.get_json()
    question.question_text = data['question_text']
    db.session.commit()
    return jsonify({'message': 'Question updated successfully!'})

@questions_bp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': 'Question deleted successfully!'})
