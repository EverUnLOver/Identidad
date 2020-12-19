"""Personas urls."""

# Django
from django.urls import path
from django.contrib.auth import views as auth_views
# Views
from identidad.personas.views import SearchView

urlpatterns = [
    # Personas
    path('search/', view=SearchView.as_view(), name='search'),

    # Users
    path('login/', auth_views.LoginView.as_view(template_name='usuarios/login.html'), name='login'),
]