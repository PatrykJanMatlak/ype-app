from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


class About(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        context = {}
        return context