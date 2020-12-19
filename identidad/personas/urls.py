"""Personas urls."""

# Urls
from django.urls import path

# Views
from identidad.personas.views import PersonasListView
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Personas
    path('search/', view=PersonasListView.as_view(), name='search'),

    # Users
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
]