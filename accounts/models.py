from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Optional fields for additional user information
    username = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=20, blank=True, null=False, unique=True)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Setting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="setting")

    # theme = models.CharField(max_length=20, default="light")
    class AlarmTime(models.IntegerChoices):
        NONE = 0, "no alarm"
        HALF = 30, "30min"
        MAXIMUM = 60, "60min"

    alarm = models.IntegerField(
        choices=AlarmTime,  # hook in the enum
        default=AlarmTime.NONE,  # default via enum member
    )
    alarm_ui = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}'s settings"
