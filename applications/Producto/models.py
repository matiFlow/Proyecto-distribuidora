from django.db import models
# Create your models here.
from applications.Proveedor.models import Proveedor

class Marca(models.Model):
    """Model definition for MODELNAME."""
    marca = models.CharField("marca del producto", max_length=50)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        """Unicode representation of Marcas."""
        return f"{self.marca}"


class Tipo(models.Model):
    """Model definition for Tipo."""
    Tipo = models.CharField("Tipo de producto", max_length=50)

    class Meta:
        """Meta definition for Tipo."""

        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        """Unicode representation of Tipo."""
        return f"{self.Tipo}"


# Create your models here.
class Producto(models.Model):
    """Model definition for Producto."""
    proveedores = models.ManyToManyField(Proveedor)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, default=0)
    precio = models.FloatField("precio de los productos", max_length=50)
    stock_actual = models.PositiveIntegerField("Existencias disponibles del producto")
    stock_minimo = models.PositiveIntegerField("Existencias minimas del producto")
    
    

    class Meta:
        """Meta definition for Producto."""

        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        """Unicode representation of Producto."""
        return f"Cateoria: {self.tipo},| Marca: {self.marca},| Precio: {self.precio},| Stock actual: {self.stock_actual},| Stock minimo: {self.stock_minimo}"
