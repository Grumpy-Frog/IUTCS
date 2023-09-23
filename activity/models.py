from django.db import models

# Create your models here.
class Activity(models.Model):
    title = models.CharField(max_length=256)
    time = models.DateTimeField()
    description = models.TextField()