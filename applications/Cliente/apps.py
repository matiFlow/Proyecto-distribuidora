# Este archivo nos sirve para configurar nestra aplicacion en particular.

from django.apps import AppConfig


class ClienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.Cliente'
