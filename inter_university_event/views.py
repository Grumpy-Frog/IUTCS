from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import Inter_University_Event

# Create your views here.
def index(request):
    inter_event = Inter_University_Event.objects.all()
    context = {'inter_event': inter_event}

    return render(request, 'inter_event/index.html', context)


def detail(request, pk):
    inter_event = Inter_University_Event.objects.get(pk=pk)
    context = {'inter_event': inter_event}

    return render(request, 'inter_event/detail.html', context)


def createInter_event(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            inter_event = Inter_University_Event()
            inter_event.title = request.POST.get('title')
            inter_event.time = request.POST.get('time')
            inter_event.content = request.POST.get('content')
            inter_event.google_form_link = request.POST.get('form_link')
            inter_event.excel_sheet_link = request.POST.get('excel_sheet_link')

            inter_event.save()

            return redirect("inter_event:inter_events")

    else:
        return render(request, 'inter_event/createinter_event.html')


class editInter_event(TemplateView):
    template_name = 'inter_event/editinter_event.html'

    def get_context_data(self, *args, **kwargs):
        inter_event = Inter_University_Event.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['inter_event'] = inter_event

        return context


def updateInter_event(request, *args, **kwargs):
    pk = kwargs.get('pk')

    inter_event = Inter_University_Event.objects.get(pk=pk)

    title = request.POST['title']
    time = request.POST['time']

    content = request.POST['content']
    form_link = request.POST['form_link']
    excel_sheet_link = request.POST['excel_sheet_link']

    inter_event.title = title
    if request.POST['time']:
        time = request.POST['time']
    else:
        time = inter_event.time

    inter_event.time = time
    inter_event.content = content
    inter_event.google_form_link = form_link
    inter_event.excel_sheet_link = excel_sheet_link

    inter_event.save()

    return HttpResponseRedirect(
        reverse("inter_event:inter_events"))


def deleteInter_event(request, *args, **kwargs):
    pk = kwargs.get('pk')
    d_inter_event = Inter_University_Event.objects.get(pk=pk)
    d_inter_event.delete()

    return HttpResponseRedirect(
        reverse("inter_event:inter_events"))


def google_formInter_event(request, pk):
    template_name = 'inter_events/google_form.html'
    inter_event = Inter_University_Event.objects.get(pk=pk)
    context = {'inter_event': inter_event}

    return render(request, template_name, context)