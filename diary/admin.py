from django.contrib import admin
from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "title", "created_time", "due_time", "ended_time")
    list_filter = ("created_time", "due_time", "ended_time")
    search_fields = ("title", "description", "user_id__username")
    ordering = ("-created_time",)
