from flask import Blueprint, request, jsonify
from config import db
from app.models import Image

images_bp = Blueprint('images', __name__)

@images_bp.route('/', methods=['POST'])
def create_image():
    data = request.get_json()
    url = data.get('url')
    image_type = data.get('type')
    if not url or not image_type:
        return jsonify({'message': 'Missing url or type'}), 400
    new_image = Image(url=url, type=image_type)
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
    image.url = data.get('url', image.url)
    image.type = data.get('type', image.type)
    db.session.commit()
    return jsonify({'message': 'Image updated successfully!'})


@images_bp.route('/sub', methods=['GET'])
def get_sub_images():
    sub_images = Image.query.filter_by(type='sub').all()
    return jsonify([image.to_dict() for image in sub_images])

@images_bp.route('/<int:id>', methods=['DELETE'])
def delete_image(id):
    image = Image.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image deleted successfully!'})
