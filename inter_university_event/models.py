from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class Inter_University_Event(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(blank=True)
    image = models.FileField(upload_to='inter_event_images', blank=True, null=True)
    maximum_member=models.IntegerField(blank=True)
    content = MDTextField()
    

class Team(models.Model):
    name = models.CharField(max_length=255)
    team_key = models.CharField(max_length=255,unique=True,blank=False)
    event = models.ForeignKey(Inter_University_Event, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    institute = models.CharField(max_length=100)

    def __str__(self):
        return self.name