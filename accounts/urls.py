
from django import urls
from . import views
from django.urls import path



urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="cadastrar-usuario"),
    
]



