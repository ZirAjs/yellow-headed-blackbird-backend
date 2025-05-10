# caffeine/admin.py

from django.contrib import admin
from .models import Caffeine


@admin.register(Caffeine)
class CaffeineAdmin(admin.ModelAdmin):
    list_display = ("id", "diary_id", "description", "amount", "timestamp")
    list_filter = ("timestamp", "diary_id")
    search_fields = ("description",)
    ordering = ("-timestamp",)
