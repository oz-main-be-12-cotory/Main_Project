from flask import Blueprint, request, jsonify
from config import db
from app.models import Question

questions_blp = Blueprint('questions', __name__, url_prefix='/questions')

@questions_blp.route('/', methods=['POST'])
def create_question():
    data = request.get_json()
    new_question = Question(
        image_id=data['image_id'],
        title=data['title'],
        sqe=data['sqe'],
        is_active=data.get('is_active', True)
    )
    db.session.add(new_question)
    db.session.commit()
    return jsonify({'message': 'Question created successfully!'}), 201

@questions_blp.route('/', methods=['GET'])
def get_questions():
    questions = Question.query.all()
    return jsonify([question.to_dict() for question in questions])

@questions_blp.route('/<int:id>', methods=['GET'])
def get_question(id):
    question = Question.query.get_or_404(id)
    return jsonify(question.to_dict())

@questions_blp.route('/<int:id>', methods=['PUT'])
def update_question(id):
    question = Question.query.get_or_404(id)
    data = request.get_json()
    question.image_id = data['image_id']
    question.title = data['title']
    question.sqe = data['sqe']
    question.is_active = data.get('is_active', question.is_active)
    db.session.commit()
    return jsonify({'message': 'Question updated successfully!'})

@questions_blp.route('/<int:id>', methods=['DELETE'])
def delete_question(id):
    question = Question.query.get_or_404(id)
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': 'Question deleted successfully!'})