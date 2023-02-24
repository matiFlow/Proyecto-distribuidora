from .models import Producto
from django import forms

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ("proveedores",'tipo','marca','precio','stock_actual','stock_minimo')
        widgets = {'proveedores': forms.SelectMultiple()}