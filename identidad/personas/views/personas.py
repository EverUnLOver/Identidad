"""Personas views."""

# Django
from django.views.generic import FormView

# Forms
from identidad.personas.forms import SearchPersonForm

class SearchView(FormView):
    """Buscador mediante el DNI."""

    template_name = 'personas/search.html'
    form_class = SearchPersonForm