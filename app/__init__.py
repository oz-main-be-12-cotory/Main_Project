from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS # 추가

from app.routes import register_routes
from config import db

migrate = Migrate()


def create_app():
    application = Flask(__name__)
    CORS(application, supports_credentials=True) # 추가: 모든 Origin 허용 및 자격 증명 허용

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

    # 400 에러 발생 시, JSON 형태로 응답 반환
    @application.errorhandler(400)
    def handle_bad_request(error):
        response = jsonify({"message": error.description})
        response.status_code = 400
        return response

    # app/route/__init__.py에 블루 브린트를 등록해주세요
    register_routes(application)

    @application.route('/')
    def index():
        return jsonify({"message": "Welcome to the OZ Form API!"})

    return application