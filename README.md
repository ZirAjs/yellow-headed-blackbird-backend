# SKYST 2025 노란머리 블랙버드 Backend Repo

## 소개

당신의 밤샘 기록, **나이테**(Night-Task) 웹 서비스의 백엔드입니다.

나이테에 대한 설명은 프론트의 [readme](https://github.com/alexander050211/yellow-headed-blackbird-frontend)를 참고해주세요.

## 기술 스택

개발
-   Django, Django REST Framework
-   gemini api

배포
-   Docker
-   SQLite
-   Nginx
-   Gunicorn
-   google-cloud-computing

### API 문서

-   [Swagger](https://hackerton.zirajs.com/swagger/)
-   [redoc](https://hackerton.zirajs.com/redoc/)

### Python dependency

```txt
djangorestframework
djangorestframework-simplejwt
drf-yasg
dotenv
gunicorn
requests
```

### Build command

```sh
# ./Build.sh
python manage.py collectstatic
docker compose up --build
```
---

오늘의 밤샘도 나이테와 함께
