from rest_framework import serializers
from .models import Diary
from tasks.models import Task
from tasks.serializers import TaskSerializer


class DiarySerializer(serializers.ModelSerializer):
    # For writing: accept list of task IDs
    tasks = serializers.ListField(child=serializers.IntegerField(), write_only=True)

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
            "tasks",  # write-only task IDs
            "task_details",  # read-only serialized task objects
        ]

    def get_task_details(self, obj):
        tasks = Task.objects.filter(diary_id=obj.id)
        return TaskSerializer(tasks, many=True).data
