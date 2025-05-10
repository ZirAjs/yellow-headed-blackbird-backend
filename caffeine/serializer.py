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
            "user_id",
            "caffeine_type",
            "amount",
            "date_time",
        ]
