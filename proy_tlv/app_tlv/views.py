from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Cliente, Proveedor
from .forms import ProveedorForm


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


#guardando data
def register_prov(request):
   form = ProveedorForm()
   if request.method == 'POST':
      form = ProveedorForm(request.POST)
      #tenemos que validar la informacion del formulario 
      if form.is_valid():
        proveedor = Proveedor()
        #tenemos que importar un modelo ----> from .models import Profesor
        #si es valido vamos a crear una instancia de profesor como?:
        proveedor.nombre_empresario = form.cleaned_data['nombre_empresario']
        #este nombre es lo que tenemos en forms.py, traeremos todolo que generamos para tener la data que vamos a guardar
        proveedor.empresa = form.cleaned_data['empresa']
        proveedor.rubro = form.cleaned_data['rubro']
        proveedor.direccion = form.cleaned_data['direccion']
        proveedor.email = form.cleaned_data['email']
        proveedor.save()
      else:
        print('datos invalidos')  
      return redirect('/home')

   context={'form':form}
   return render(request, 'app_tlv/register_prov.html', context=context)
