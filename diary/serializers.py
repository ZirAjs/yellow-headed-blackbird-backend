from rest_framework import serializers
from .models import Diary


class DiarySerializer(serializers.ModelSerializer):
    # Write-only: for creating/updating with a list of task IDs
    tasks = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Diary
        fields = [
            "id",
            "user_id",
            "title",
            "description",
            "focus_time",
            "tasks",
        ]
