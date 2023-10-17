from django.views.generic import TemplateView

from inter_university_event.models import Inter_University_Event, Team, Member
from intra_university_event.models import Intra_University_Event


class HomePage(TemplateView):
    template_name = 'base.html'


class ExecutiveCommittee(TemplateView):
    template_name = 'ExecutiveCommittee.html'


class about(TemplateView):
    template_name = 'about.html'


class home(TemplateView):
    template_name = 'home.html'

class leaderboard(TemplateView):
    template_name = 'leaderboard.html'

class events(TemplateView):
    template_name = 'events.html'

class inter_event_participants(TemplateView):
    template_name = 'events_and_participants.html'

    def get_context_data(self, *args, **kwargs):
        inter_university_event = Inter_University_Event.objects.all()
        intra_university_event = Intra_University_Event.objects.all()

        teams = Team.objects.all()
        members = Member.objects.all()

        context = super().get_context_data(*args, **kwargs)

        context['inter_event'] = inter_university_event
        context['teams'] = teams
        context['members'] = members
        context['intra_event'] = intra_university_event

        #df = pd.read_csv('https://docs.google.com/spreadsheets/d/1huzjXqhw-JQYZ7P1fkbdtd7uyYYe9NN-LeUlGS4lX6I/edit?usp=sharing')
        #print(df)

        return context

class intra_event_participants(TemplateView):
    template_name = 'events_and_participants2.html'

    def get_context_data(self, *args, **kwargs):
        
        intra_university_event = Intra_University_Event.objects.all()


        context = super().get_context_data(*args, **kwargs)

        context['intra_event'] = intra_university_event


        return context