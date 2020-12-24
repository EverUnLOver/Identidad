"""Personas model."""

# Django
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

class Personas(AbstractUser):
    """Personas model.

    Un modelo creado para almacenar la informacion de las personas con DNI.
    """

    # Informacion primordial
    nombre = models.CharField(max_length=20)
    segundo_nombre = models.CharField(max_length=20)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    DNI = models.CharField(max_length=30, unique=True, 
        error_messages={
            'unique': 'This DNI already exists.'
        }
    )
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
    estado_civil = models.ForeignKey('personas.EstadoCivil', on_delete=models.SET_NULL, null=True)

    USERNAME_FIELD = 'DNI'
    REQUIRED_FIELDS = ['celular','username', 'email']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.nombre, self.primer_apellido, self.segundo_apellido)
        if self.segundo_nombre:
            full_name = '%s %s %s %s' % (self.nombre, self.segundo_nombre, self.primer_apellido, self.segundo_apellido)
        return full_name.strip()

    def __str__(self):
        return str('Nombre: '+self.username+', DNI: '+self.DNI)
    
    class Meta:
        ordering = ('username',)