from django.contrib import admin
from .models import Diary


@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    list_display = ("id", "user_id", "title", "focus_time")
    search_fields = ("title", "description", "user_id__username")
    list_filter = ("user_id",)
