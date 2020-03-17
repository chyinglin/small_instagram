from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from small_instagram.models import Post


# Create your views here.
class Helloworld(TemplateView):
    template_name = 'test.html'


class PostView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'make_post.html'
    fields = '__all__'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
