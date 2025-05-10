# SKYST 2025 노란머리 블랙버드 – Backend Repository

## 프로젝트 소개

이 저장소는 밤샘 기록 웹 서비스 **나이테(Night-Task)**의 백엔드입니다.
당신의 모든 야근과 집중의 순간을 함께합니다.

👉 서비스 및 기능에 대한 자세한 내용은 [프론트엔드 리포지토리 README](https://github.com/alexander050211/yellow-headed-blackbird-frontend)를 참고하세요.

---

## 기술 스택

### 백엔드 개발

* **Django**, **Django REST Framework**
* **Gemini API** 연동

### 배포 환경

* **Docker**
* **SQLite**
* **Nginx**
* **Gunicorn**
* **Google Cloud Computing**

---

## 📄 API 문서

* [Swagger 문서 보기](https://hackerton.zirajs.com/swagger/)
* [ReDoc 문서 보기](https://hackerton.zirajs.com/redoc/)

---

## Python 의존성

```txt
djangorestframework
djangorestframework-simplejwt
drf-yasg
dotenv
gunicorn
requests
```

---

## Build 명령어

```sh
# 실행: ./Build.sh
python manage.py collectstatic
docker compose up --build
```

---

## 🌙 끝없는 밤샘의 동반자, 나이테와 함께하세요.

