from rest_framework.serializers import ModelSerializer
from .models import Diary


class DiarySerializer(ModelSerializer):
    class Meta:
        model = Diary
        fields = ["id", "user_id", "title", "description", "focus_time"]
