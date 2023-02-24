from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'Producto.app'

urlpatterns = [
    path(
        "producto/lista/",
        views.ProductoListView.as_view(),
        name = 'Listado de productos'
    ),
    path(
        "producto/buscar/",
        views.BuscarProductoListView.as_view(),
        name="Buscar producto"
    ),
    
    path(
        "producto/crear/",
        views.ProductoCreateView.as_view(),
        name="Crear producto"
    ),
    path(
        "producto/detalle/pk/",
        views.ProductoDetailView.as_view(),
        name="Detalle del producto"
    ),

    path(
        "producto/delete/",
        views.ProductoDeleteView.as_view(),
        name="Eliminar producto"
    ),

    path(
        "producto/modificar/pk/",
        views.ProductoUpdateView.as_view(),
        name='Modificar producto'
    ),
]