from django.shortcuts import render
from .models import Task

import requests
import json
import re

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import permission_classes
from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

# openapi
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

GEMINI_API_URL = settings.GEMINI_API_URL
GEMINI_API_KEY = settings.GEMINI_API_KEY


@permission_classes([IsAuthenticated])
class TasksViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(diary_id__user_id=user.id)


@permission_classes([AllowAny])
class GenerateTasksView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                "title",
                openapi.IN_QUERY,
                description="Task title",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "description",
                openapi.IN_QUERY,
                description="Task description",
                type=openapi.TYPE_STRING,
            ),
            openapi.Parameter(
                "final_time",
                openapi.IN_QUERY,
                description="Final time",
                type=openapi.TYPE_STRING,
            ),
        ]
    )
    def get(self, request):
        title = request.query_params.get("title")
        description = request.query_params.get("description")
        final_time = request.query_params.get("final_time")

        if not title:
            return Response({"error": "title은 필수입니다."}, status=400)
        if not final_time:
            return Response({"error": "final_time은 필수입니다."}, status=400)

        prompt = f"""
당신은 작업(Task) 생성 도우미입니다.

다음은 사용자가 입력한 제목과 설명입니다:

제목: {title}
설명: {description}
최종 마감 시간: {final_time}

이 정보를 바탕으로 다음 필드를 포함한 Task를 여러 개 생성하세요 (최소 3개).
- title
- order (int, 순서대로)
- due_time (UTC ISO 8601 형식, 목표 종료 시간)
- type (string, 무조건 "middle")
JSON 배열 형식으로 출력하세요.
        """

        headers = {"Content-Type": "application/json"}
        data = {"contents": [{"parts": [{"text": prompt}]}]}

        response = requests.post(
            f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", headers=headers, json=data
        )

        if response.status_code != 200:
            return Response(
                {"error": "Gemini API 호출 실패", "detail": response.text}, status=500
            )

        try:
            generated_text = response.json()["candidates"][0]["content"]["parts"][0][
                "text"
            ]
            json_string = re.search(
                r"```json\s*(.*?)\s*```", generated_text, re.DOTALL
            ).group(1)
            task_list = json.loads(json_string)
        except Exception as e:
            return Response(
                {"error": f"Gemini 응답 파싱 실패 {response.text}", "detail": str(e)},
                status=500,
            )

        return Response(task_list, status=200)
