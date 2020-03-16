from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from small_instagram.models import Post


# Create your views here.
class Helloworld(TemplateView):
    template_name = 'test.html'


class PostView(ListView):
    model = Post
    template_name = 'index.html'
