from django.forms import ModelForm
from django import forms

from .models import Inter_University_Event

class InterUniversityEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




    class Meta:
        model = Inter_University_Event
        fields = ['content']