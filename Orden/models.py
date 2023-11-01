from django.db import models
from Mesa.models import Mesa
from Plato.models import Plato

# Create your models here.

class Orden(models.Model):
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)

    plato = models.ManyToManyField(Plato)
