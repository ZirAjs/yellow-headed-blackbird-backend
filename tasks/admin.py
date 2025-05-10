from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "diary_id",
        "title",
        "order",
        "due_time",
        "start_time",
        "finished_time",
    )
    list_filter = ("due_time", "finished_time", "start_time")
    search_fields = ("title", "description", "diary_id__title")
    ordering = ("order", "due_time")
