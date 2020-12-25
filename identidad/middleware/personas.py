"""Middleware para el admin."""

# Django
from django.http import response
from django.shortcuts import redirect
from django.urls import reverse

class AdminPathMiddleware:
    """NUeva ruta para admin despues del log in."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Codigo para cambiar la ruta."""
        if not request.user.is_staff:
            if request.path == '/admin/':
                return redirect('/admin/personas/')

        response = self.get_response(request)
        return response
        