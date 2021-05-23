from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

class HomePage(TemplateView):
    template_name = 'index.html'

class AboutPage(TemplateView):
    template_name = 'about.html'
