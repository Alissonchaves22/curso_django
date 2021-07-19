from django.shortcuts import render
from django.urls import conf
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from .models import Post
from blog import models

class BlogListView(ListView):
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['titulo', 'conteudo', 'autor']


class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['titulo', 'conteudo'] 


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')