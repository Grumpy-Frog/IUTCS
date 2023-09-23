from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class Event(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField()
    content = MDTextField()