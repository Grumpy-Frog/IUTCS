import os

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Intra_University_Event
from .forms import IntraUniversityEventForm


# Create your views here.
def index(request):
    intra_event = Intra_University_Event.objects.all()
    context = {'intra_event': intra_event}

    return render(request, 'intra_events/index.html', context)


def detail(request, pk):
    intra_event = Intra_University_Event.objects.get(pk=pk)
    context = {'intra_event': intra_event}

    return render(request, 'intra_events/detail.html', context)


'''
def createIntra_event(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            intra_event = Intra_University_Event()
            intra_event.title = request.POST.get('title')
            intra_event.time = request.POST.get('time')
            intra_event.content = request.POST.get('content')
            intra_event.google_form_link = request.POST.get('form_link')
            intra_event.excel_sheet_link = request.POST.get('excel_sheet_link')

            intra_event.save()

            return redirect("intra_event:intra_events")

    else:
        return render(request, 'intra_events/createintra_event.html')
'''


def createIntra_event(request):
    form = IntraUniversityEventForm
    if request.method == 'POST':
        form = IntraUniversityEventForm(request.POST)

        if form.is_valid():
            if request.POST.get('title') and request.POST.get('content'):
                intra_event = Intra_University_Event()
                intra_event.title = request.POST.get('title')
                intra_event.time = request.POST.get('time')
                intra_event.google_form_link = request.POST.get('form_link')
                intra_event.excel_sheet_link = request.POST.get('excel_sheet_link')

                dir = "/media/"
                image = request.FILES['image']
                fss = FileSystemStorage()
                print(image.name)
                file = fss.save(image.name, image)
                file_url = fss.url(file)
                intra_event.image = dir + os.path.basename(file_url)

                content = form.cleaned_data['content']
                intra_event.content = content

                intra_event.save()

                return redirect("intra_event:intra_events")

    context = {'form': form}

    return render(request, 'intra_events/createintra_event.html', context)


class editIntra_event(TemplateView):
    template_name = 'intra_events/editintra_event.html'

    def get_context_data(self, *args, **kwargs):
        intra_event = Intra_University_Event.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['form'] = IntraUniversityEventForm(instance=intra_event)
        context['intra_event'] = intra_event

        return context


def updateIntra_event(request, *args, **kwargs):
    pk = kwargs.get('pk')

    intra_event = Intra_University_Event.objects.get(pk=pk)

    title = request.POST['title']
    time = request.POST['time']

    content = request.POST['content']
    form_link = request.POST.get('google_form_link')
    sheet_link = request.POST['excel_sheet_link']
    intra_event.title = title
    if request.POST['time']:
        time = request.POST['time']
    else:
        time = intra_event.time

    intra_event.time = time
    intra_event.content = content
    intra_event.google_form_link = form_link
    intra_event.excel_sheet_link = sheet_link

    dir = "/media/"
    image = request.FILES['image']
    fss = FileSystemStorage()
    print(image.name)
    file = fss.save(image.name, image)
    file_url = fss.url(file)
    intra_event.image = dir + os.path.basename(file_url)


    intra_event.save()

    return HttpResponseRedirect(
        reverse("intra_event:intra_events"))


def deleteIntra_event(request, *args, **kwargs):
    pk = kwargs.get('pk')
    d_intra_event = Intra_University_Event.objects.get(pk=pk)
    d_intra_event.delete()

    return HttpResponseRedirect(
        reverse("intra_event:intra_events"))


def google_formIntra_event(request, pk):
    template_name = 'intra_events/google_form.html'
    intra_event = Intra_University_Event.objects.get(pk=pk)
    context = {'intra_event': intra_event}

    return render(request, template_name, context)
