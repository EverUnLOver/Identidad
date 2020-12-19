# Django
import django_filters

# Models
from identidad.personas.models import Personas

class PersonasFilter(django_filters.FilterSet):
    class Meta:
        model = Personas
        fields = '__all__'