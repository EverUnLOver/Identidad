"""Personas urls."""

# Django
from django.urls import path

# Views
from identidad.personas.views import SearchView

urlpatterns = [
    # Personas
    path(route='search/', view=SearchView.as_view(), name='search')
]