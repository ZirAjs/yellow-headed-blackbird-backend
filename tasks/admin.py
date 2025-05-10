# tasks/admin.py

from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "diary",
        "order",
        "due_time",
        "start_time",
        "finished_time",
        "type",
    )
    list_filter = ("type", "due_time", "diary")
    search_fields = ("title", "type", "diary__title")
    ordering = ("diary", "order")
