#El archivo admin nos sirve para añadir un panel de administrador a nuestras aplicacion. Este panel nos permite administrar, crear usuarios, realizar acciones en nuestras aplicaciones, etc.

from django.contrib import admin
from .models import Cliente, Carrito

admin.site.register(Cliente)
admin.site.register(Carrito)
# Register your models here.
