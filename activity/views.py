import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView

from .models import Activity


# Create your views here.

def index(request):
    activity = Activity.objects.all()
    context = {'activity': activity}

    return render(request, 'activity/index.html', context)


def createActivity(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            activity = Activity()
            activity.title = request.POST.get('title')
            activity.time = request.POST.get('time')
            activity.description = request.POST.get('content')

            activity.save()

            return redirect("activity:activity")

    else:
        return render(request, 'activity/createActivity.html')


class editActivity(TemplateView):
    template_name = 'activity/editActivity.html'

    def get_context_data(self, *args, **kwargs):
        activity = Activity.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['activity'] = activity

        return context


def updateActivity(request, *args, **kwargs):
    pk = kwargs.get('pk')

    activity = Activity.objects.get(pk=pk)

    title = request.POST['title']
    if request.POST['time']:
        time = request.POST['time']
    else:
        time = activity.time
    description = request.POST['content']

    activity.title = title
    activity.time = time
    activity.description = description

    activity.save()

    return HttpResponseRedirect(
        reverse("activity:activity"))


def deleteActcity(request, *args, **kwargs):
    pk = kwargs.get('pk')
    d_activity = Activity.objects.get(pk=pk)
    d_activity.delete()

    return HttpResponseRedirect(
        reverse("activity:activity"))

