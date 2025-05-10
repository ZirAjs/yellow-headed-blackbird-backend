from django.contrib import admin
from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "title", "created_at", "ended_at")
    list_filter = ("created_at", "ended_at")
    search_fields = (
        "title",
        "description",
        "user_id__email",
    )  # Adjust based on User model
    ordering = ("-created_at",)
