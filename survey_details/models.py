from django.db import models
from datetime import datetime


class SurveyEntry(models.Model):
    location = models.CharField(max_length=50, null=False)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    Comment = models.TextField()
    media = models.FileField(null=True)


