from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    diary_id = serializers.IntegerField(source="diary_id.id")

    def validate(self, data):
        # do basic validation
        super().validate(data)

        # check if the diary_id belongs to the user
        user = self.context["request"].user
        diary_id = data.get("diary_id")
        if not user.diaries.filter(id=diary_id).exists():
            raise serializers.ValidationError("Diary does not belong to the user.")

    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "diary_id",
            "order",
            "due_time",
            "start_time",
            "finished_time",
        ]
