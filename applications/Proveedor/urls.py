from django.contrib import admin
from django.urls import path, re_path, include
from . import views

app_name = 'Proveedor.app'

urlpatterns = [
    path(
        "proveedor/lista/",
        views.ProveedorListView.as_view(),
        name = 'Listado de proveedores'
    ),
    path(
        "proveedor/buscar/",
        views.BuscarProveedorListView.as_view(),
        name="Buscar proveedor"
    ),
    
    path(
        "proveedor/crear/",
        views.ProveedorCreateView.as_view(),
        name="Crear proveedor"
    ),
    path(
        "proveedor/detalle/<pk>/",
        views.ProductoDetailView.as_view(),
        name="Detalle del proveedor"
    ),

    path(
        "proveedor/eliminar/<pk>/",
        views.ProveedorDeleteView.as_view(),
        name="Eliminar proveedor"
    ),

    path(
        "proveedor/modificar/<pk>/",
        views.ProveedorUpdateView.as_view(),
        name='Modificar proveedor'
    ),
]