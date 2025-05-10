from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .services.sun_api import fetch_sun_info

# Create your views here.
@permission_classes([AllowAny])
class NatureEventsView(APIView):
    def get(self, request):
        base_day_param = request.GET.get("base_day")
        try:
            base_date = datetime.strptime(base_day_param, "%Y-%m-%d").date()
            next_date = base_date + timedelta(days=1)
        except ValueError:
            return Response({"error": "Invalid base_day format. Use YYYY-MM-DD."}, status=400)
        
        lat = float(request.GET.get("lat", 37.5665))
        lng = float(request.GET.get("lng", 126.9780))

        sun_data = fetch_sun_info(lat=lat, lng=lng, base_date=str(base_date), next_date = str(next_date))

        events = [
            {
                "type": "sunrise",
                "time": sun_data["sunrise"].isoformat(),
                "description": "해가 뜨는 시간"
            },
            {
                "type": "sunset",
                "time": sun_data["sunset"].isoformat(),
                "description": "해가 지는 시간"
            }
        ]

        # TODO : bird 가져오는 거 추가

        events.sort(key=lambda x: datetime.fromisoformat(x["time"]))

        return Response(events)
