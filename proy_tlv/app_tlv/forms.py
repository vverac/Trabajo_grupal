from django import forms
from .models import Proveedor

#estoy creando desde models proveedor
class ProveedorForm(forms.ModelForm):
  class Meta:
      model= Proveedor
      # fields = ['nombre','direccion','email']
      # es lo mismo estamos usando todos los datos
      fields = '__all__'
# tenemos que tener el modelo de escuela en este caso
