from flask import Blueprint, request, jsonify, Response
import boto3
from urllib.parse import urlparse
from config import db
from app.models import Image

images_blp = Blueprint('images', __name__, url_prefix='/images')

@images_blp.route('/', methods=['POST'])
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

@images_blp.route('/', methods=['GET'])
def get_images():
    images = Image.query.all()
    return jsonify([image.to_dict() for image in images])

@images_blp.route('/<int:id>', methods=['GET'])
def get_image(id):
    image = Image.query.get_or_404(id)
    return jsonify(image.to_dict())

@images_blp.route('/<int:id>', methods=['PUT'], strict_slashes=False)
def update_image(id):
    image = Image.query.get_or_404(id)
    data = request.get_json()
    image.url = data.get('url', image.url)
    image.type = data.get('type', image.type)
    db.session.commit()
    return jsonify({'message': 'Image updated successfully!'})


@images_blp.route('/sub', methods=['GET'], strict_slashes=False)
def get_sub_images():
    sub_images = Image.query.filter_by(type='sub').all()
    return jsonify([image.to_dict() for image in sub_images])

@images_blp.route('/proxy')
def image_proxy():
    s3_url = request.args.get('url')
    if not s3_url:
        return "URL parameter is required", 400

    try:
        # Parse the S3 URL to get bucket name and key
        parsed_url = urlparse(s3_url)
        bucket_name = parsed_url.netloc.split('.')[0]
        key = parsed_url.path.lstrip('/')

        # Use boto3 to get the object from S3
        s3 = boto3.client('s3')
        s3_object = s3.get_object(Bucket=bucket_name, Key=key)
        image_data = s3_object['Body'].read()
        content_type = s3_object['ContentType']

        return Response(image_data, content_type=content_type)

    except Exception as e:
        return str(e), 500


@images_blp.route('/main', methods=['GET'], strict_slashes=False)
def get_main_image():
    main_image = Image.query.filter_by(type='main').first_or_404()
    return jsonify(main_image.to_dict())

@images_blp.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
def delete_image(id):
    image = Image.query.get_or_404(id)
    db.session.delete(image)
    db.session.commit()
    return jsonify({'message': 'Image deleted successfully!'})