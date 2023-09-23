import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, DetailView, TemplateView
from .models import Achievement


# Create your views here.

def index(request):
    achievement = Achievement.objects.all()
    context = {'achievement': achievement}

    return render(request, 'achievements/index.html', context)


def createAchievement(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            post = Achievement()
            post.title = request.POST.get('title')
            post.description = request.POST.get('content')
            dir = "/media/"
            image = request.FILES['image']
            fss = FileSystemStorage()
            print(image.name)
            file = fss.save(image.name, image)
            file_url = fss.url(file)
            post.image = dir + os.path.basename(file_url)

            post.save()

            return redirect("achievements:achievements")

    else:
        return render(request, 'achievements/createAchievement.html')


class editAchievement(TemplateView):
    template_name = 'achievements/editAchievement.html'

    def get_context_data(self, *args, **kwargs):
        achievement = Achievement.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['achievement'] = achievement

        return context


def updateAchievement(request, *args, **kwargs):
    pk = kwargs.get('pk')
    # print(pk)
    # post = Achievement.objects.get(pk=pk)
    post = Achievement.objects.get(pk=pk)

    title = request.POST['title']
    description = request.POST['content']


    try:
        dir = "/media/"
        image = request.FILES['image']
        fss = FileSystemStorage()
        # print(image.name)
        file = fss.save(image.name, image)
        file_url = fss.url(file)
        image = dir + os.path.basename(file_url)
    except:
        image = post.image


    post.title = title
    post.image = image
    post.description = description

    post.save()

    return HttpResponseRedirect(
        reverse("achievements:achievements"))

def deleteAchievement(request, *args, **kwargs):
    pk = kwargs.get('pk')
    d_achievement = Achievement.objects.get(pk=pk)
    d_achievement.delete()

    return HttpResponseRedirect(
        reverse("achievements:achievements"))