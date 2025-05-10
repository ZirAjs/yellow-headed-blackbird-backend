from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Optional fields for additional user information
    username = models.EmailField(max_length=255, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=20, blank=True, null=False, unique=True)

    def __str__(self):
        return self.username
