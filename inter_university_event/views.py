from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from django.core.files.storage import FileSystemStorage

from .models import Inter_University_Event,Team,Member
from .forms import InterUniversityEventForm

import os
from datetime import datetime
import random
import string

from django.core.mail import send_mail
from IUT_CS.settings import EMAIL_HOST_USER

# Create your views here.
def index(request):
    inter_event = Inter_University_Event.objects.all()
    context = {'inter_event': inter_event}

    return render(request, 'inter_event/index.html', context)


def detail(request, pk):
    inter_event = Inter_University_Event.objects.get(pk=pk)
    context = {'inter_event': inter_event}

    return render(request, 'inter_event/detail.html', context)

'''
def createInter_event(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content'):
            inter_event = Inter_University_Event()
            inter_event.title = request.POST.get('title')
            inter_event.time = request.POST.get('time')
            inter_event.content = request.POST.get('content')

            inter_event.save()

            return redirect("inter_event:inter_events")

    else:
        return render(request, 'inter_event/createinter_event.html')

'''



def createInter_event(request):
    form = InterUniversityEventForm
    if request.method == 'POST':
        form = InterUniversityEventForm(request.POST)

        if form.is_valid():
            if request.POST.get('title') and request.POST.get('content'):
                inter_event = Inter_University_Event()
                inter_event.title = request.POST.get('title')
                inter_event.time = request.POST.get('time')
                inter_event.maximum_member = request.POST.get('maximum_member')


                dir = "/media/"
                image = request.FILES['image']
                fss = FileSystemStorage()
                print(image.name)
                file = fss.save(image.name, image)
                file_url = fss.url(file)
                inter_event.image = dir + os.path.basename(file_url)

                content = form.cleaned_data['content']
                inter_event.content = content

                inter_event.save()

                return redirect("inter_event:inter_events")

    context = {'form': form}

    return render(request, 'inter_event/createinter_event.html', context)


class editInter_event(TemplateView):
    template_name = 'inter_event/editinter_event.html'

    def get_context_data(self, *args, **kwargs):
        inter_event = Inter_University_Event.objects.get(pk=self.kwargs.get('pk'))
        context = super().get_context_data(*args, **kwargs)

        context['form'] = InterUniversityEventForm(instance=inter_event)
        context['inter_event'] = inter_event

        return context


def updateInter_event(request, *args, **kwargs):
    pk = kwargs.get('pk')

    inter_event = Inter_University_Event.objects.get(pk=pk)

    title = request.POST['title']
    time = request.POST['time']
    maximum_member = request.POST['maximum_member']

    content = request.POST['content']

    inter_event.title = title
    if request.POST['time']:
        time = request.POST['time']
    else:
        time = inter_event.time

    dir = "/media/"
    image = request.FILES['image']
    fss = FileSystemStorage()
    print(image.name)
    file = fss.save(image.name, image)
    file_url = fss.url(file)
    inter_event.image = dir + os.path.basename(file_url)

    inter_event.time = time
    inter_event.content = content
    inter_event.maximum_member = maximum_member
    
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


def team_registration(request, pk):
    inter_event = Inter_University_Event.objects.get(pk=pk)
    context = {'inter_event': inter_event}

    if request.method == 'POST':
        if request.POST.get('team_name'):
            team = Team()
            team.name = request.POST.get('team_name')
            team.event = inter_event

            timestamp = int(datetime.timestamp(datetime.now()))
            random_string = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
            unique_key = f"{timestamp}-{random_string}"
            team.team_key = unique_key

            team.save()
            
            members=[]
            for i in range(0,inter_event.maximum_member):
                member = Member()
                member.team = team
                member.name = request.POST.get('member_'+ str(i) + '_name')
                member.email = request.POST.get('member_'+ str(i) + '_email')
                member.phone = request.POST.get('member_'+ str(i) + '_phone')
                member.institute = request.POST.get('member_'+ str(i) + '_institute')

                if len(member.name)!=0 and len(member.email)!=0 and len(member.phone)!=0 and len(member.institute)!=0:
                    member.save()
                    
            
                members.append(member)
            
            context = {'inter_event':inter_event}
            context['team']=team
            context['members']=members


            subject = 'Tnx for registration for'+str(inter_event.title) 
            message = str(team.name)+'\nThank you for registering on our event.\n'+ 'This is your team key: '+ str(team.team_key)
            from_email = EMAIL_HOST_USER
            recipient_list = []
            for mem in members:
                recipient_list.append(mem.email)  # Replace with the user's email address
            
            send_mail(subject, message, from_email, recipient_list)

            
            return redirect("inter_event:inter_events")
            
    else:
        return render(request, 'inter_event/team_registration_page.html', context)
    


