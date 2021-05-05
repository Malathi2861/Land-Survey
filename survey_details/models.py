from django.db import models
# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
from datetime import datetime


# Create your models here.


class SurveyEntry(models.Model):
    location = models.CharField(max_length=50)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    Comment = models.TextField()
    media = models.FileField(upload_to='media/', null=True, verbose_name="")


