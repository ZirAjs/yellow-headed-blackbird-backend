from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action

from django.utils import timezone
from datetime import datetime, time, timedelta

from .models import Diary
from .serializers import DiarySerializer, DiaryDetailSerializer

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

    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the diaries
        for the currently authenticated user.
        """
        user = self.request.user
        return Diary.objects.filter(user_id=user.id)

    def create(self, request, *args, **kwargs):
        """
        Create a new diary entry.
        """
        user_id = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        diary = serializer.save(user_id=user_id)
        diary.save()

        return Response(serializer.data, status=201)

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a diary entry by its ID.
        """
        instance = self.get_object()
        serializer = DiaryDetailSerializer(instance)

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
