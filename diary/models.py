from django.db import models


class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    focus_time = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
