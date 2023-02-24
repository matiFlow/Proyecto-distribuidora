"""persona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#En este archivo se escriben las url que los usuarios pueden visitar

from django.contrib import admin
from django.urls import path,re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('',include('applications.Cliente.urls')), #Con include, django dice que estas determinadas url pertenecen a esta aplicacion, entonces que vallan a esta carpeta.
    re_path('', include('applications.Producto.urls')), #Las cadenas vacias sirven para indicar que antes de la url no va a ir nada
    re_path('', include('applications.Proveedor.urls')),
]

#Include nos sirve para que las aplicaciones guarden sus propias url que les correspone. 


















