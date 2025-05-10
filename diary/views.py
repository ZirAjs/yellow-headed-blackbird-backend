from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Diary
from .serializers import DiarySerializer


class DiaryViewSet(ModelViewSet):
    """
    A viewset for viewing and editing diary instances.
    """

    queryset = Diary.objects.all()
    serializer_class = DiarySerializer
    permission_classes = [IsAuthenticated]
