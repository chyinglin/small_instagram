from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
class Helloworld(TemplateView):
    template_name = 'test.html'
