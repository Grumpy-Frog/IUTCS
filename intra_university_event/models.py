from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class Intra_University_Event(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(blank=True)
    content = MDTextField()
    google_form_link = models.URLField(max_length=512, db_index=True, unique=True, blank=True)
