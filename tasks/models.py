from django.db import models

# Create your models here.
class Task(models.Model):
    diary = models.ForeignKey('diary.Diary', on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    due_time = models.DateTimeField()
    start_time = models.DateTimeField()
    finished_time = models.DateTimeField()
    type = models.CharField(max_length=200)