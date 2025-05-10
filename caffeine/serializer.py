from rest_framework import serializers
from .models import Caffeine


class CaffeineSerializer(serializers.ModelSerializer):
    """
    Serializer for the Caffeine model.
    """

    class Meta:
        model = Caffeine
        fields = [
            "id",
            "diary_id",
            "amount",
            "date_time",
            "description",
        ]
