from .models import Cliente
from django import forms


class ClienteForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ('nombre','apellido','telefono','dni', 'carrito')
        widgets = {'carrito': forms.SelectMultiple()}

"""
class CarritoForm(forms.ModelForm):
    class Meta:
        model = Producto
        widgets = ('productos_disponibles')
"""

    
