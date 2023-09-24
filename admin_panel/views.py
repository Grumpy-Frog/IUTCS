import os

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from achievements.models import Achievement

# Create your views here.
def AdminPanel(request):
    return render(request, 'admin_panel/index.html')
