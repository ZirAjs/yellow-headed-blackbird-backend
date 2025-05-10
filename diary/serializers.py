from rest_framework import serializers
from .models import Diary
from tasks.models import Task
from tasks.serializers import TaskSerializer
from accounts.models import User


class DiarySerializer(serializers.ModelSerializer):
    # For writing: accept list of task IDs
    tasks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user_id = serializers.IntegerField(source="user_id.id", read_only=True)
    due_at = serializers.DateTimeField(allow_null=False, required=True)

    # For reading: show actual task data
    task_details = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Diary
        fields = [
            "id",
            "user_id",
            "title",
            "description",
            "focus_time",
            "due_at",
            "created_at",
            "ended_at",
            "tasks",  # read-only task IDs
            "task_details",  # read-only serialized task objects
        ]

    def get_task_details(self, obj):
        tasks = Task.objects.filter(diary_id=obj.id)
        return TaskSerializer(tasks, many=True).data
