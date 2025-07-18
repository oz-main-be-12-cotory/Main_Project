# 각 route에서 블루프린트를 만들어주세요
# stats_routes_blp를 참고해주시면 됩니다!
from .answers import answers_bp
from .choices import choices_bp
from .questions import questions_bp
from .stats_routes import stats_routes_blp
from .users import users_bp
from .images import images_bp


def register_routes(application):
    application.register_blueprint(answers_bp)
    application.register_blueprint(choices_bp)
    application.register_blueprint(questions_bp)
    application.register_blueprint(stats_routes_blp)
    application.register_blueprint(users_bp)
    application.register_blueprint(images_bp)
