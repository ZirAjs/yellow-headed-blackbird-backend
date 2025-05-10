from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import permission_classes

from .serializer import CaffeineSerializer
from .models import Caffeine


@permission_classes([IsAuthenticated])
class CaffeineViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing caffeine instances.
    """

    serializer_class = CaffeineSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the caffeine
        for the currently authenticated user.
        """
        user = self.request.user
        return Caffeine.objects.filter(user_id=user.id)
