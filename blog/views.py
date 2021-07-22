from django.core.checks import messages
from django.db.models import fields
from django.shortcuts import render
from django.urls import conf
from django.urls.base import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView
from .models import Post
from blog import models

from django.dispatch import receiver
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm

class BlogListView(ListView):
    
    model = Post
    template_name = 'blog/home.html'


class BlogDetailView(DetailView):
    
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post_detail'

class BlogCreateView(LoginRequiredMixin,SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Post
    form_class = PostForm
    template_name = 'blog/post_new.html'
    #fields = ['autor', 'titulo', 'conteudo']
    success_message = "%(field)s - cadastrado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field = self.object.titulo,
        )



class BlogUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'
    #fields = ['titulo', 'conteudo'] 
    success_message = "%(field)s - alterado com sucesso"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.autor = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            field = self.object.titulo,
        )


class BlogDeleteView(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')
    success_message = "Removido com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(BlogDeleteView, self).delete(request, *args, **kwargs)

    


