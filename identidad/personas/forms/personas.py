"""Persona forms."""

# Django
from django import forms
from django.core.validators import RegexValidator
from django.forms import widgets

# Models
from identidad.personas.models import Personas

class PersonForm(forms.Form):
    """Formulario personas.

    Este formulario esta diseñado para ayudar al frontend a crear la pagina donde se proporciona
    nuevo contenido de DNI.
    """

    # Informacion primordial
    nombre = forms.CharField(max_length=20, min_length=2)
    segundo_nombre = forms.CharField(max_length=20, min_length=2)
    primer_apellido = forms.CharField(max_length=20, min_length=2)
    segundo_apellido = forms.CharField(max_length=20, min_length=2)
    nombre_completo = forms.CharField()
    DNI = forms.CharField(max_length=20, min_length=5)

    # Informacion de contacto
    celular = forms.CharField(help_text='Numero del celular personal', max_length=17, min_length=11, required=False)
    telefono = forms.CharField(help_text='Numero telefonico del hogar', max_length=7, min_length=7, required=False)
    email = forms.EmailField(help_text='Direccion de correo electronico', required=False)

    #Informacion extra
    estados_civiles = (
        ('SOLTERO', 'Soltero'),
        ('CASADO', 'Casado'),
        ('COMPROMETIDO', 'Comprometido'),
        ('AVENTURERO', 'Aventurero')
    )
    estado_civil = forms.TypedMultipleChoiceField(choices=estados_civiles)

    def save(self):
        data = self.cleaned_data
        DNI = self.cleaned_data['DNI']
        try:
            persona = Personas.objects.get(DNI=DNI)
        except Personas.DoesNotExist:
            persona = Personas.objects.create(**data)
        raise forms.ValidationError('Ya hay alguien con este DNI.')

class SearchPersonForm(forms.Form):
    """Se emplea para la busqueda de personas mediante el DNI."""

    DNI = forms.CharField()

    def clean_search(self):
        try:
            persona = Personas.objects.get(DNI=self.cleaned_data['DNI'])
        except Personas.DoesNotExist:
            raise forms.ValidationError('Este DNI aun no esta registrado.')
        return persona
    
