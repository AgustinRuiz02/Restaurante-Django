from django.urls import path
from . import views

urlpatterns = [
    path('', views.mesaHome, name='mesaHome'),
    path('mesaNueva', views.mesaNueva, name='mesaNueva'),
    path('listaMesas', views.listaMesas, name='listaMesas')
]