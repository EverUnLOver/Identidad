"""Modelo de estado civil."""

# Django
from django.db import models

class EstadoCivil(models.Model):
    """Modelo para crear y almacenar estados civiles."""
    estado_civil = models.CharField(max_length=20)
    
    def __str__(self):
        return '%s' % (self.estado_civil)