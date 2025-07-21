# Feature: 1.0.0 (1차 수정)

# app/models.py (모든 ERD 테이블 구조에 맞춰 수정)
# app/__init__.py (들여쓰기 및 라우트 import 위치 수정)
# app/routes/answers.py (db import 경로 수정)
# app/routes/choices.py (db import 경로 수정)
# app/routes/images.py (db import 경로 수정)
# app/routes/questions.py (db import 경로 수정)
# app/routes/stats_routes.py (db import 경로 및 Choices를 Choice로 수정)
# app/routes/users.py (db import 경로 수정)
# config.py (SQLALCHEMY_DATABASE_URI 플레이스홀더로 수정)
# requirements.txt (새로 설치된 패키지 반영)


# README.md
# Feature: 1.0.1 (2차 수정)

# 데이터베이스 마이그레이션 성공:
# config.py의 데이터베이스 연결 정보(DB 이름, 사용자/비밀번호) 문제를 해결했습니다.
# flask db migrate 및 flask db upgrade 명령을 성공적으로 실행하여 ERD에 정의된 테이블 구조를 MySQL 데이터베이스에 반영했습니다.