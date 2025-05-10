from django.shortcuts import render

import os
import requests
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.conf import settings

GEMINI_API_URL = settings.GEMINI_API_URL
GEMINI_API_KEY = settings.GEMINI_API_KEY

class GenerateTasksFromTextView(APIView):
    def post(self, request):
        title = request.data.get("title")
        description = request.data.get("description")

        if not title:
            return Response({"error": "title은 필수입니다."}, status=400)

        prompt = f"""
당신은 작업(Task) 생성 도우미입니다.

다음은 사용자가 입력한 제목과 설명입니다:

제목: {title}
설명: {description}

이 정보를 바탕으로 다음 필드를 포함한 Task를 여러 개 생성하세요 (최소 3개).
- title
- order (int, 순서대로)
- due_time (UTC ISO 8601 형식)
- start_time (UTC ISO 8601 형식)
- finished_time (UTC ISO 8601 형식, 예상 종료 시간)
- type (string, 무조건 "middle")
JSON 배열 형식으로 출력하세요.
        """

        headers = {"Content-Type": "application/json"}
        data = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=data
        )

        if response.status_code != 200:
            return Response({"error": "Gemini API 호출 실패", "detail": response.text}, status=500)

        try:
            generated_text = response.json()['candidates'][0]['content']['parts'][0]['text']
            task_list = json.loads(generated_text)
        except Exception as e:
            return Response({"error": "Gemini 응답 파싱 실패", "detail": str(e)}, status=500)

        return Response(task_list, status=200)
