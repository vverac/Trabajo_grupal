from django.urls import path
from . import views
# from django.views.generic import TemplateView
from app_tlv.views import IndexView


urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('clientes/', views.cliente_list, name='clientes'),
    path('proveedores/', views.register_prov, name='proveedores')
]
