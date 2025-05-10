from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Cutoff


class UserAdmin(BaseUserAdmin):
    # Optional: Customize how the fields are shown
    fieldsets = BaseUserAdmin.fieldsets + (
        (
            "Custom Fields",
            {"fields": ()},  # Add any custom fields here like 'phone_number'
        ),
    )
class CutoffAdmin(admin.ModelAdmin):
    list_display = ('name', 'cut')

admin.site.register(User, UserAdmin)
admin.site.register(Cutoff, CutoffAdmin)
