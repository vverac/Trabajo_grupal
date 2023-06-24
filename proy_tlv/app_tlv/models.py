
# Create your models here.
from django.db import models

# Create your models here.
# from django.conf import settings
# from django.utils import timezone


class Cliente(models.Model):
  # def __init__(self, nombre, edad):
      nombre = models.CharField(max_length=100)
      apellido =  models.CharField(max_length=100)
      edad = models.CharField(max_length=100)
      direccion = models.CharField(max_length=50)
      email = models.EmailField()
      
      def __str__(self):
        return self.nombre


class Proveedor(models.Model):
  # def __init__(self, nombre, edad):
      nombre_empresario = models.CharField(max_length=100)
      empresa =  models.CharField(max_length=100)
      rubro = models.CharField(max_length=100)
      direccion = models.CharField(max_length=50)
      email = models.EmailField()
      
      def __str__(self):
        return self.empresa