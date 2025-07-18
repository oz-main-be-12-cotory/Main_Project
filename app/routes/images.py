from flask import Blueprint, request, jsonify
from app import db
from app.models import Image

images_bp = Blueprint('images', __name__)

@images_bp.route('/', methods=['POST'])
def create_image():
    data = request.get_json()
    new_image = Image(question_id=data['question_id'], image_url=data['image_url'])
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'message': 'Image created successfully!'}), 201

@images_bp.route('/', methods=['GET'])
def get_images():
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])

@images_bp.route('/<int:id>', methods=['GET'])
def get_image(id):
    image = Image.query.get_or_404(id)
    return jsonify(image.to_dict())

@images_bp.route('/<int:id>', methods=['PUT'])
def update_image(id):
    image = Image.query.get_or_404(id)
    data = request.get_json()
    image.question_id = data['question_id']
    image.image_url = data['image_url']
    db.session.commit()
    return jsonify({'message': 'Image updated successfully!'})

@images_bp.route('/<int:id>', methods=['DELETE'])
def delete_image(id):
    image = Image.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image deleted successfully!'})
