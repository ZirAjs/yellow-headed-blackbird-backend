# SKYST 2025 노란머리 블랙버드 – Backend Repository

![header](https://capsule-render.vercel.app/api?type=wave&color=111111&height=300&section=header&text=Night-Task&fontColor=ffffff&fontSize=90)

## 프로젝트 소개

이 저장소는 밤샘 기록 웹 서비스 **나이테(Night-Task)** 의 백엔드입니다.
당신의 모든 야근과 집중의 순간을 함께합니다.

👉 서비스 및 기능에 대한 자세한 내용은 [프론트엔드 리포지토리 README](https://github.com/alexander050211/yellow-headed-blackbird-frontend)를 참고하세요.

## 기술 스택
<div align=center>
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white">
<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
<img src="https://img.shields.io/badge/django%20rest%20framework-ff1709?style=for-the-badge&logo=django&logoColor=white"/>
</div>
<div align=center>
<img src="https://img.shields.io/badge/sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white"/>
<img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white"/>
<img src="https://img.shields.io/badge/gunicorn-499848?style=for-the-badge&logo=gunicorn&logoColor=white"/>
<img src="https://img.shields.io/badge/google%20cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white"/>
</div>
<div align=center>
<img src="https://img.shields.io/badge/swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black"/>
</div>

### 백엔드 개발

* **Django**, **Django REST Framework**
* **Gemini API** 연동

### 배포 환경

* **Docker**
* **SQLite**
* **Nginx**
* **Gunicorn**
* **Google Cloud Computing**


## 📄 API 문서

* [Swagger 문서 보기](https://hackerton.zirajs.com/swagger/)
* [ReDoc 문서 보기](https://hackerton.zirajs.com/redoc/)


## Python 의존성

```txt
djangorestframework
djangorestframework-simplejwt
drf-yasg
dotenv
gunicorn
requests
```


## Build 명령어

```sh
# 실행: ./Build.sh
python manage.py collectstatic
docker compose up --build
```
## 백엔드 기능 상세

### 📍 유저 정보 저장

### 🤖 gemini를 이용한 밤샘 계획 제안

이번 밤샘해서 달성해야 할 목표와 마감시간을 입력하면 세부계획을 제안해주는 간단한 인공지능 기능을 도입했습니다

### ☕ 유저의 밤샘 기록 저장

열정 넘치던 순간의 기억을 소중히 저장합니다. 카페인 섭취량, 목표 달성 시간 등을 저장합니다

### 🌅 일출/일몰시간 제공

sunrise-sunset 를 이용해 일출과 일몰 시간을 제공합니다

### 🐦 새들의 응원메세지 전달

힘들었지만 무사히 밤샘을 마친 당신에게 새들이 당신을 축하해줍니다. 종료시간에 따라 달라지는 응원메세지를 전달합니다.

---

## 🌙 끝없는 밤샘의 동반자, 나이테와 함께하세요.

![footer](https://capsule-render.vercel.app/api?type=wave&color=111111&height=300&section=header&text=Night-Task&fontColor=ffffff&fontSize=90)