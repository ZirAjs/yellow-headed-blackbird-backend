from rest_framework import serializers
from .models import Task
from diary.models import Diary


class TaskSerializer(serializers.ModelSerializer):
    diary_id = serializers.PrimaryKeyRelatedField(queryset=Diary.objects.all())

    def validate(self, data):
        # do basic validation
        data = super().validate(data)

        # check if the diary_id belongs to the user
        user = self.context["request"].user
        diary = data.get("diary_id")
        if not user.diaries.filter(id=diary.id).exists():
            raise serializers.ValidationError("Diary does not belong to the user.")

        return data

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
