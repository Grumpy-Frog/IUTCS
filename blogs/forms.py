from django.forms import forms
from mdeditor.fields import MDTextFormField

from blogs.models import Blog


class MDEditorForm(forms.Form):
    name = forms.CharField()
    content = MDTextFormField()


class MDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
