from django.db import models
from diary.models import Diary


# Create your models here.
class Task(models.Model):
    diary_id = models.ForeignKey(Diary, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField()
    due_time = models.DateTimeField()
    start_time = models.DateTimeField(auto_now_add=True)
    finished_time = models.DateTimeField(null=True, blank=True)
