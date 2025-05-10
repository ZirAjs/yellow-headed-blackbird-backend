from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "diary_id",
        "order",
        "due_time",
        "start_time",
        "finished_time",
    )
    list_filter = ("diary_id", "due_time", "start_time", "finished_time")
    search_fields = ("title", "description")
    ordering = ("order",)
