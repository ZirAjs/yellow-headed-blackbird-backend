from django.db import models


# Create your models here.
class Caffeine(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("", on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    amount = models.FloatField()
    date_time = models.DateTimeField(auto_now_add=True)
