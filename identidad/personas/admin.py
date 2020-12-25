"""Admin personas."""

# Django
# Django
from django.contrib import admin

# Models
from .models import Personas, EstadoCivil


@admin.register(Personas)
class PersonasAdmin(admin.ModelAdmin):
    """Personas admin model."""

    list_display = ('username', 'DNI', 'email', 'estado_civil')

    fieldsets = (
        ('Persona',{
            'fields': (
                ('username', 'estado_civil'),
                ('DNI')
            ),
        }),
    )
admin.site.register(EstadoCivil)