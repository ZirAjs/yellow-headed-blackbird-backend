from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from django.utils.dateparse import parse_datetime
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .services.sun_api import fetch_sun_info
from .models import Bird
import random

# Create your views here.
@permission_classes([AllowAny])
class NatureEventsView(APIView):
    def get(self, request):
        start_datetime_param = request.GET.get("start_date_time")
        end_datetime_param = request.GET.get("end_date_time")
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
                "type": "sunrise",
                "name": "sun",
                "time": sun_data["sunrise"].isoformat(),
                "description": "해가 뜨는 시간"
            },
            {
                "type": "sunset",
                "name": "sun",
                "time": sun_data["sunset"].isoformat(),
                "description": "해가 지는 시간"
            }
        ]

        while current_dt < end_dt:
            next_dt = current_dt + timedelta(hours=1)

            # 해당 시간 구간에 포함된 Bird 객체 필터링
            birds_in_range = Bird.objects.filter(date_time__gte=current_dt, date_time__lt=next_dt)
            if birds_in_range.exists():
                bird = random.choice(list(birds_in_range))
                events.append({
                    "type": "bird",
                    "name": bird.name,
                    "time": bird.time.isoformat(),
                    "description": bird.description,
                })
            
            current_dt = next_dt

        events.sort(key=lambda x: datetime.fromisoformat(x["time"]))

        return Response(events)
