from django.contrib import admin
from .models import Bird

@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ("name", "time", "description")
    search_fields = ("name", "description")
    list_filter = ("name", "time")