"""Personas model."""

# Django
from django.db import models
from django.core.validators import RegexValidator

class Personas(models.Model):
    """Personas model.

    Un modelo creado para almacenar la informacion de las personas con DNI.
    """

    # Informacion primordial
    nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20, )
    segundo_apellido = models.CharField(max_length=20, )
    nombre_completo = models.CharField(max_length=70)
    DNI = models.CharField(max_length=30)

    # Informacion de contacto
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message='Phone number must be entered in the format: +999999999. Up to 15 digits allowed.'
    )
    celular = models.CharField('Numero del celular personal', validators=[phone_regex], max_length=17, blank=True)
    telefono = models.CharField('Numero telefonico del hogar', max_length=7, blank=True)
    email = models.EmailField('Direccions de correo electronico', unique=True, 
        error_messages={
            'unique': 'Ya hay un usuario asociado a este correo.'
        }
    )

    #Informacion extra
    estados_civiles = (
        ('SOLTERO', 'Soltero'),
        ('CASADO', 'Casado'),
        ('COMPROMETIDO', 'Comprometido'),
        ('AVENTURERO', 'Aventutero')
    )
    estado_civil = models.CharField(choices=estados_civiles, max_length=12)

    def __str__(self):
        return str('Nombre: '+self.nombre_completo+', DNI: '+self.DNI)