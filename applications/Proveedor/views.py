from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView, DetailView
from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.
from django.urls import reverse_lazy



class Inicio(TemplateView):
    template_name = "inicio.html"

class ProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/lista.html"
    ordering = 'nombre'
    context_object_name = 'proveedores'

class BuscarProveedorListView(ListView):
    model = Proveedor
    template_name = "proveedor/buscar.html"
    ordering = 'nombre'
    context_object_name = 'proveedor'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Proveedor.objects.filter(
            nombre__icontains = palabra_clave
        )
        return lista

class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = "proveedor/crear.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('Proveedor.app: Listado de proveedores')
    
    def  form_valid(self, form):
        return super(ProveedorCreateView, self).form_valid(form)
    
    
class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = "proveedor/modificar.html"
    form_class = ProveedorForm
    success_url = reverse_lazy('Proveedor.app: Listado de proveedores')
    
    def  form_valid(self, form):
        pr = form.save(comit=False)
        pr.nombre_completo = pr.nombre + '' + pr.apellido
        pr.save()
        return super(ProveedorCreateView, self).form_valid(form)

class ProductoDetailView(DetailView):
    model = Proveedor
    template_name = "proveedor/detalle.html"
    ordering = 'nombre'
    context_object_name = 'proveedor'


class ProveedorDeleteView(DeleteView, DetailView):
    model = Proveedor
    template_name = "eliminar.html"

class BuscarProductoListView(ListView):
    model = Proveedor
    template_name = "prooveedor/buscar.html"
    ordering = 'apellido'
    context_object_name = 'prooveedores'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Proveedor.objects.filter(
            apellido__icontains = palabra_clave
        )
        return lista




