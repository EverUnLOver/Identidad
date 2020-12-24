"""Personas views."""

# Django
from django.views.generic import FormView

# Forms
from identidad.personas.forms import SearchPersonForm

# Filters
from identidad.personas.filters import PersonasFilter

# Views
from django.views.generic import ListView

# Models
from identidad.personas.models import Personas

class PersonasListView(ListView):
    """Lista de personas""" 

    model = Personas
    ordering = ('-username',)
    template_name = 'personas/search.html'
    context_object_name = 'personas'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PersonasFilter(self.request.GET, queryset=self.get_queryset())
        return context
