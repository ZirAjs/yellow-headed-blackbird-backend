from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta, time
from django.db.models import Q
from django.utils.dateparse import parse_datetime
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .services.sun_api import fetch_sun_info
from .models import Bird
import random
from django.utils import timezone

# Create your views here.
@permission_classes([AllowAny])
class NatureEventsView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('start_date_time', openapi.IN_QUERY, description="시작 날짜시간 (예: 2025-05-10T22:00:00)", type=openapi.TYPE_STRING),
            openapi.Parameter('end_date_time', openapi.IN_QUERY, description="끝 날짜시간 (예: 2025-05-11T04:00:00)", type=openapi.TYPE_STRING),
        ],
        responses={200: 'nature event 리스트 반환', 400: '잘못된 요청'},
        operation_description="해당 시간 구간 내의 일출, 일몰, 새 활동목록을 반환",
    )

    def get(self, request):
        start_dt = parse_datetime(request.GET.get("start_date_time"))
        end_dt = parse_datetime(request.GET.get("end_date_time"))
        
        if not start_dt or not end_dt:
            return Response({"error": "Invalid datetime"}, status=400)
        
        try:
            base_date = start_dt.date()
            next_date = base_date + timedelta(days=1)
        except ValueError:
            return Response({"error": "Invalid base_day format. Use YYYY-MM-DD."}, status=400)
        
        lat = float(request.GET.get("lat", 37.5665))
        lng = float(request.GET.get("lng", 126.9780))

        sun_data = fetch_sun_info(lat=lat, lng=lng, base_date=str(base_date), next_date = str(next_date))

        events = [
            {
                "type": "sunset",
                "name": "sun",
                "time": timezone.make_aware(sun_data["sunset"]).isoformat(),
                "description": "해가 지는 시간"
            },
            {
                "type": "sunrise",
                "name": "sun",
                "time": timezone.make_aware(sun_data["sunrise"]).isoformat(),
                "description": "해가 뜨는 시간"
            }
        ]

        end_hour = end_dt.time().hour
        active_birds = Bird.objects.filter(time__hour=end_hour)
        if active_birds.exists():
            bird = random.choice(list(active_birds))
            events.append({
                    "type": "bird",
                    "name": bird.name,
                    "time": end_dt.isoformat(),
                    "description": bird.description,
                })
        else:
            events.append({
                    "type": "bird",
                    "name": "노란머리블랙버드",
                    "time": end_dt.isoformat(),
                    "description": "노란머리블랙버드가 여러분을 응원합니다",
                })
        
        return Response(events)
