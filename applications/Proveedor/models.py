from django.db import models
# Create your models here.


# Create your models here.
class Proveedor(models.Model):
    """Model definition for Provedoor."""
    nombre = models.CharField("Nombre del proveedor",max_length=50)
    apellido = models.CharField(("Apellido del proveedor"), max_length=50)
    cuit = models.IntegerField("Cuit del proveedor")
    telefono = models.IntegerField("Telefono del proveedor")

    class Meta:
        """Meta definition for Provedoor."""

        verbose_name = 'Provedor'
        verbose_name_plural = 'Provedoors'

    def __str__(self):
        """Unicode representation of Provedoor."""
        return f"Nombre:{self.nombre}  Apellido:{self.apellido}   Cuit:{self.cuit}   Telefono: {self.telefono}"

    
    