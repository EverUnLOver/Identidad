# Django
import django_filters

# Models
from identidad.personas.models import Personas

class PersonasFilter(django_filters.FilterSet):

    CHOICES = (
        ('ascending', 'Ascending'),
        ('descending', 'Descending')
    )

    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')

    class Meta:

        model = Personas
        fields = {
            'DNI': ['icontains'],
            'username': ['icontains'],
            'estado_civil': ['exact'],
        }
    
    def filter_by_order(self, queryset, name, value):
        expression = 'date_joined' if value == 'ascending' else '-date_joined'
        return queryset.order_by(expression)