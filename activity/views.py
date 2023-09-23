import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Activity
# Create your views here.

def index(request):
    activity = Activity.objects.all()
    context = {'activity': activity}

    return render(request, 'activity/index.html', context)


def createAchievement(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Activity()
            post.title = request.POST.get('title')
            post.description = request.POST.get('content')

            post.save()

            return redirect("activity:create_activity")

    else:
        return render(request, 'achievements/createAchievement.html')


class editActivity(TemplateView):
    template_name = 'activity/editAchievement.html'

    def get_context_data(self, *args, **kwargs):
        activity = Activity.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['activity'] = activity

        return context


def updateActivity(request, *args, **kwargs):
    pk = kwargs.get('pk')

    activity = Activity.objects.get(pk=pk)

    title = request.POST['title']
    description = request.POST['content']




    activity.title = title

    activity.description = description

    activity.save()

    return HttpResponseRedirect(
        reverse("activity:update_activity"))
