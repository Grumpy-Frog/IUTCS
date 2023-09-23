from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'base.html'


class ExecutiveCommittee(TemplateView):
    template_name = 'ExecutiveCommittee.html'