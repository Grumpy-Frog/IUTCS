from django.forms import ModelForm
from django import forms

from intra_university_event.models import Intra_University_Event

class IntraUniversityEventForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




    class Meta:
        model = Intra_University_Event
        fields = ['content']