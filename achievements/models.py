from django.db import models

# Create your models here.
class Achievement(models.Model):
    title = models.CharField(max_length=256)
    image = models.FileField(upload_to='achievement_images', blank=True, null=True)
    description = models.TextField()