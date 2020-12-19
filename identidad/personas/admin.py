"""Admin personas."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from .models import Personas


@admin.register(Personas)
class PersonasAdmin(admin.ModelAdmin):
    """Personas admin model."""

    list_display = ('username', 'DNI', 'email')

    fieldsets = (
        ('Persona',{
            'fields': (
                ('username'),
                ('DNI')
            ),
        }),
    )