from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Setting, Tier


class UserAdmin(BaseUserAdmin):
    model = User
    list_display = ("username", "nickname", "experience", "is_staff", "is_superuser")
    list_filter = ("is_staff", "is_superuser", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("nickname", "experience")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "nickname",
                    "experience",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("username",)
    ordering = ("username",)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ("user", "alarm", "alarm_ui")
    list_filter = ("alarm", "alarm_ui")


@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ("name", "cut")
    search_fields = ("name",)


admin.site.register(User, UserAdmin)
