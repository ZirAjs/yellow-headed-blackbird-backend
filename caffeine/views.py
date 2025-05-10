from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from .serializers import CaffeineSerializer
from .models import Caffeine


@permission_classes([IsAuthenticated])
class CaffeineViewSet(
    GenericViewSet,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
):
    serializer_class = CaffeineSerializer

    def get_queryset(self):
        user = self.request.user

        return Caffeine.objects.filter(diary_id__user_id=user.id)
