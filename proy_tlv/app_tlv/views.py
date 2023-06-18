from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Cliente

# Create your views here.
# def index_estatico(request):
#   return render(request, 'paginas/landing.html')

# def formulario_contacto(request):
#   return render(request, 'paginas/contacto.html')

class IndexView(TemplateView):
  template_name='app_tlv/landing.html'

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'app_tlv/cliente_list.html', {'clientes': clientes})
