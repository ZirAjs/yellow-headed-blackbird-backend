from django.db import models
from diary.models import Diary


# Create your models here.
class Caffeine(models.Model):
    id = models.AutoField(primary_key=True)
    diary_id = models.ForeignKey(
        Diary, on_delete=models.CASCADE, related_name="caffeine"
    )
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
