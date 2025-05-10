# SKYST 2025 노란머리 블랙버드 Backend Repo

## 소개

SKYST 2025 노란머리 블랙버드의 Backend Repo입니다.

## 기술 스택

-   Django
-   Django REST Framework
-   Docker
-   SQLite
-   Nginx
-   Gunicorn
-   google-cloud-computing
-   gemini api

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
