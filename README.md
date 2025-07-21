# Feature: 1.0.0 (1차 수정)

## app/models.py (모든 ERD 테이블 구조에 맞춰 수정)

## app/__init__.py (들여쓰기 및 라우트 import 위치 수정)

## app/routes/answers.py (db import 경로 수정)

## app/routes/choices.py (db import 경로 수정)

## app/routes/images.py (db import 경로 수정)

## app/routes/questions.py (db import 경로 수정)

## app/routes/stats_routes.py (db import 경로 및 Choices를 Choice로 수정)

## app/routes/users.py (db import 경로 수정)

## config.py (SQLALCHEMY_DATABASE_URI 플레이스홀더로 수정)

## requirements.txt (새로 설치된 패키지 반영)


## Feature: 1.0.1 (2차 수정)

## 데이터베이스 마이그레이션 성공

## config.py의 데이터베이스 연결 정보(DB 이름, 사용자/비밀번호) 문제 해결

## flask db migrate 및 flask db upgrade 명령 실행하여 ERD에 정의된 테이블 구조를 MySQL 데이터베이스에 반영


## Feature: 1.0.2 (3차 수정)

## 이미지 생성/수정 API (`POST /images`, `PUT /images/<id>`): Image 모델의 url 및 type 필드를 처리하도록 수정.
## 이미지 생성 및 수정 시 type (예: 'main', 'sub') 지정 가능
## 서브 이미지 조회 API (`GET /images/sub`): type이 sub인 이미지만을 조회하는 새로운 엔드포인트 추가


## Feature: 1.0.3 (4차 수정)

## 브랜치 충돌을 방지하기 위해 병합 및 커밋을 수행
## 풀리퀘스트 생성 및 테스트 진행
## Develop 브랜치에 변경사항 적용 및 테스트

## Develop 1.0.0

## CORS 문제 해결: 프론트엔드와 백엔드 간의 CORS 문제를 해결하기 위해 백엔드(app/__init__.py)의 CORS 설정에 supports_credentials=True 옵션을 추가

## 질문 페이지 문제 진단 및 해결 제안: 질문 페이지에서 질문이 표시되지 않는 문제를 파악.

## 프론트엔드(QuestionPage.jsx)가 질문을 sqe (순서)로 요청하지만, 백엔드(app/routes/questions.py)는 id로 질문을 처리하는 불일치가 원인으로 파악 됨. 

