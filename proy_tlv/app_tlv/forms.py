from django import forms
from .models import Proveedor

#estoy creando desde models proveedor
class ProveedorForm(forms.ModelForm):
  class Meta:
      model= Proveedor
      fields = '__all__'


class LoginForm(forms.Form):
  nombre = forms.CharField(widget=forms.TextInput)
  password = forms.CharField(widget=forms.PasswordInput)

