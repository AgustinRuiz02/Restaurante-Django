from django.db import models

# Create your models here.

class Mesa(models.Model):

    numeroMesa = models.IntegerField()

    #estado = models.BooleanField(default=False)
