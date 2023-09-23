from django.contrib import admin

from django.db import models
from .models import Blogs
from mdeditor.widgets import MDEditorWidget

class ExampleModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

# Register your models here.
admin.site.register(Blogs,ExampleModelAdmin )