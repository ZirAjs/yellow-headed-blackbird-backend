from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Diary
from .serializers import DiarySerializer


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

    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a diary entry by its ID.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
