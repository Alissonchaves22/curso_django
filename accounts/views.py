from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import UserCreationFormWithEmail
from django.urls.base import reverse_lazy

class SignUpView(generic.CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


