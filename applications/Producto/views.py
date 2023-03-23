from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView, DetailView
from .models import Producto
from .forms import ProductoForm
# Create your views here.
from django.urls import reverse_lazy



class Inicio(TemplateView):
    template_name = "inicio.html"

class ProductoListView(ListView):
    model = Producto
    template_name = "producto/lista.html"
    ordering = 'tipo'
    context_object_name = 'productos'

class BuscarProductoListView(ListView):
    model = Producto
    template_name = "producto/buscar.html"
    ordering = 'marca'
    context_object_name = 'productos'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Producto.objects.filter(
            marca__icontains = palabra_clave
        )
        return lista

class ProductoCreateView(CreateView):
    model = Producto
    template_name = "producto/crear.html"
    form_class = ProductoForm
    success_url = reverse_lazy('Producto.app: Lista de productos')
    
    def  form_valid(self, form):
        return super(ProductoCreateView, self).form_valid(form)
    
    
class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "producto/update.html"
    form_class = ProductoForm
    success_url = reverse_lazy('Producto.app: Listado de productos')
    
    def  form_valid(self, form):
        pr = form.save(comit=False)
        pr.nombre_completo = pr.tipo + '' + pr.marca
        pr.save()
        return super(ProductoCreateView, self).form_valid(form)


class ProductoDeleteView(DeleteView, DetailView):
    model = Producto
    template_name = "delete.html"

class ProductoDetailView(DetailView):
    model = Producto
    template_name = "producto/detalle.html"
    ordering = 'tipo'
    context_object_name = 'detalle'