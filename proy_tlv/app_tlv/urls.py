from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from app_tlv.views import IndexView


urlpatterns = [
    path('home/', IndexView.as_view(), name='home'),
    path('clientes/', views.cliente_list, name='clientes'),
    path('proveedores/', views.register_prov, name='proveedores'),
    # path('login/', views.login, name='login'),
    path('bienvenido/', views.bienvenido, name='home'),
    path('register_user/', views.register_user, name='register_user'),
    path('login/', LoginView.as_view(template_name='app_tlv/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='app_tlv/logout.html'), name='logout'),

]
