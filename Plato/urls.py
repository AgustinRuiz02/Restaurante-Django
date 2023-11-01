from django.urls import path
from . import views

urlpatterns = [
    path('', views.platoHome, name='platoHome'),
    path('platoNuevo', views.platoNuevo, name='platoNuevo'),
    path('listaPlatos', views.listaPlatos, name='listaPlatos')
]