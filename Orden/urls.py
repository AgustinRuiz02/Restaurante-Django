from django.urls import path
from . import views

urlpatterns = [
    path('', views.ordenHome, name='ordenHome'),
    path('ordenNueva', views.ordenNueva, name='ordenNueva'),
    path('listaOrdenes', views.listaOrdenes, name='listaOrdenes')
]