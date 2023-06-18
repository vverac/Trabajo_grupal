from django.urls import path
from . import views
# from django.views.generic import TemplateView
from app_tlv.views import IndexView
from .views import cliente_list

urlpatterns = [
    path('', IndexView.as_view()),
    path('clientes/', cliente_list, name='cliente_list')
]
