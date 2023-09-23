from django import forms
from mdeditor.fields import MDTextFormField
from mdeditor.widgets import MDEditorWidget

from blogs.models import Blogs


class MDEditorForm(forms.Form):
    name = forms.CharField()
    content = forms.CharField(widget=MDEditorWidget)


class MDEditorModleForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = '__all__'
