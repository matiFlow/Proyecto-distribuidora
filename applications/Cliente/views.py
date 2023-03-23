#Desde aqui vamos a enviar la informacion que queremos que vea el usuario

from django.views.generic import ListView, DeleteView, CreateView, TemplateView, UpdateView, DetailView
from .models import Cliente
from .forms import ClienteForm
# Create your views here.
from django.urls import reverse_lazy



class Inicio(TemplateView):
    template_name = "inicio.html"

class ClienteListView(ListView):
    model = Cliente
    template_name = "cliente/lista.html"
    ordering = 'apellido'
    context_object_name = 'clientes'

class BuscarClienteListView(ListView):
    model = Cliente
    template_name = "cliente/buscar.html"
    ordering = 'apellido'
    context_object_name = 'clientes'

    def get_queryset(self):
        palabra_clave = self.request.GET.get('kword','')
        lista = Cliente.objects.filter(
            apellido__icontains = palabra_clave
        )
        return lista

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = "cliente/crear.html"
    form_class = ClienteForm
    success_url = reverse_lazy('Cliente.app: Lista de clientes')
    
    def  form_valid(self, form):
        return super(ClienteCreateView, self).form_valid(form)
    
    
class ClienteUpdateView(UpdateView):
    model = Cliente
    template_name = "cliente/modificar.html"
    form_class = ClienteForm
    success_url = reverse_lazy('Cliente.app: Lista de clientes')
    
    def  form_valid(self, form):
        cl = form.save(comit=False)
        cl.nombre_completo = cl.nombre + '' + cl.apellido
        cl.save()
        return super(ClienteCreateView, self).form_valid(form)

class ClienteDeleteView(DeleteView, DetailView):
    model = Cliente
    template_name = "cliente/eliminar.html"



class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "cliente/detalle.html"
    ordering = 'apellido'
    context_object_name = 'detalle'
    





