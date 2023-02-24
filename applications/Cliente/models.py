#Esta aplicacion nos permite crear clases, y esas clases se convierten en tablas de SQL. ORM se encarga de crear estas tablas y modificarlas.

from django.db import models

from applications.Producto.models import Producto

# Create your models here.

class Carrito(models.Model):
    """Model definition for Carrito."""
    carrito = models.ForeignKey(Producto, on_delete=models.CASCADE, default="No realizo ninguna compra", blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Carrito."""

        verbose_name = 'Carrito'
        verbose_name_plural = 'Carritos'

    def __str__(self):
        """Unicode representation of Carrito."""
        return f"{self.carrito}"


class Cliente(models.Model):
    """campos"""
    nombre = models.CharField("Nombre del cliente", max_length=50)
    apellido = models.CharField("Apellido del cliente", max_length=50)
    nombre_completo = models.CharField("Nombre completo", max_length=50, default='')
    telefono = models.IntegerField("Telefono del cliente")
    dni = models.IntegerField("Dni del cliente")
    carrito = models.ManyToManyField(Carrito, verbose_name="Compra del cliente")

    class Meta:
        "Permite agregar informacion al modelo Cliente"
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    
    def __str__(self) -> str:
        "Representacion de cada registro de Cliente"
        "Muestra el registro de las tablas"
        return f"Nombre: {self.nombre} | Apellido: {self.apellido} | telefono: {self.telefono} | DNI: {self.dni} | Compra: {self.carrito}" 
        
        



