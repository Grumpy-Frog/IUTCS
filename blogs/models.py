from django.db import models

# Create your models here.
from django.db import models
from mdeditor.fields import MDTextField

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    content = MDTextField()
    created_at = models.DateTimeField(auto_now_add=True)