from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from django.db.models import Prefetch


from django.utils import timezone, dateparse
from datetime import datetime, time, timedelta

from .models import Diary
from .serializers import DiarySerializer, DiaryDetailSerializer

##############################
# Swagger Config             #
##############################
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

start_param = openapi.Parameter(
    "start_datetime",
    openapi.IN_QUERY,
    description="Start datetime for filtering diaries ",
    type=openapi.TYPE_STRING,
    format="date-time",
)

end_param = openapi.Parameter(
    "end_datetime",
    openapi.IN_QUERY,
    description="End datetime for filtering diaries ",
    type=openapi.TYPE_STRING,
    format="date-time",
)

################################

# Internal cache
_cached_6pm = None
_cached_timestamp = None
CACHE_DURATION = timedelta(minutes=10)


def get_today_6pm():
    global _cached_6pm, _cached_timestamp

    now = timezone.now()

    if (
        _cached_6pm is None
        or _cached_timestamp is None
        or (now - _cached_timestamp > CACHE_DURATION)
    ):
        # Compute most recent 6 PM
        today_6pm = timezone.make_aware(datetime.combine(now.date(), time(18, 0)))
        if now < today_6pm:
            today_6pm -= timedelta(days=1)

        _cached_6pm = today_6pm
        _cached_timestamp = now

    return _cached_6pm


class DiaryViewSet(ModelViewSet):
    """
    A viewset for viewing and editing diary instances.
    """

    http_method_names = ["get", "post", "patch", "delete"]
    serializer_class = DiaryDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return diaries for the authenticated user, optionally filtered by datetime range.
        Prefetch tasks and caffeine entries for serializer efficiency.
        """
        user = self.request.user
        start_datetime = self.request.query_params.get("start_datetime")
        end_datetime = self.request.query_params.get("end_datetime")

        queryset = Diary.objects.filter(user_id=user.id)

        if start_datetime and (
            start_datetime := dateparse.parse_datetime(start_datetime)
        ):
            queryset = queryset.filter(created_time__gte=start_datetime)

        if end_datetime and (end_datetime := dateparse.parse_datetime(end_datetime)):
            queryset = queryset.filter(created_time__lte=end_datetime)

        return queryset.order_by("-created_time")

    @swagger_auto_schema(manual_parameters=[start_param, end_param])
    def list(self, request, *args, **kwargs):
        """
        List all diary entries for the authenticated user.
        """
        queryset = self.get_queryset()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset, request)

        serializer = DiarySerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Create a new diary entry.
        **주의** ended_time 생성시 diary가 즉시 종료되기에 생성할 때는 비워두어야 합니다.
        """
        user_id = request.user
        serializer = DiarySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        diary = serializer.save(user_id=user_id)
        diary.save()

        return Response(serializer.data, status=201)

    def partial_update(self, request, *args, **kwargs):
        """
        Update a diary entry.
        """
        instance = self.get_object()
        serializer = DiaryDetailSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # only allow modification of title, description, focus_time, due_time

        if "ended_time" in request.data:
            # add experience to user
            user = request.user
            duration = timezone.now() - instance.created_time
            minutes = int(duration.total_seconds() // 60)
            print(f"minutes: {minutes}")
            user.experience += minutes
            user.save()
            serializer.save(
                ended_time=timezone.now(),
                created_time=instance.created_time,
            )  # override with server time
        else:
            serializer.save(created_time=instance.created_time)  # proceed as usual

        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def winners(self, request):
        """
        Get the winners of the diaries.
        [percent] means the user has left the app as top [percent] of the users.
        """
        today_6pm = get_today_6pm()
        total_diaries = Diary.objects.filter(created_time__gt=today_6pm).count()
        if total_diaries == 0:
            return Response({"percent": 0.0})
        else:
            finished_diaries = Diary.objects.filter(
                ended_time__gt=today_6pm,
                created_time__gt=today_6pm,
            ).count()
            percent = 1 - (float(finished_diaries) / total_diaries)
            return Response({"percent": percent})
