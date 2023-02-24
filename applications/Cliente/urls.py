#Aqui se añadiran las rutas de url

from django.contrib import admin
from django.urls import path #Path 
                                                    
from . import views

app_name = 'Cliente.app'

urlpatterns = [ #Va a tener una gran lista de modulos path.
    path( # path es una estructura
        "inicio/", #nombre de direccion de la pagina
        views.Inicio.as_view(), #La vista que se va a utilizar, se coloca el nombre de la clase
        name = 'Pagina inicial' #Nombre de la pagina
    ),
    
    path(
        "cliente/lista/",
        views.ClienteListView.as_view(),
        name = 'Listado de clientes'
    ),
    path(
        "cliente/buscar/",
        views.BuscarClienteListView.as_view(),
        name="Buscar cliente"
    ),
    
    path(
        "cliente/crear/",
        views.ClienteCreateView.as_view(),
        name="Crear Cliente"
    ),
    path(
        "cliente/detalle/<pk>/",
        views.ClienteDetailView.as_view(),
        name="Detalle del cliente"
    ),

    path(
        "cliente/delete/<pk>/",
        views.ClienteDeleteView.as_view(),
        name="Eliminar cliente"
    ),

    path(
        "cliente/modificar/<pk>/",
        views.ClienteUpdateView.as_view(),
        name='Modificar cliente'
    ),
]
