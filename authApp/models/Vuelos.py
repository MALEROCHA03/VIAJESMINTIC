from django.db import models


class Vuelos(models.Model):
    IdVuelo = models.AutoField(primary_key=True)
    aerolinea = models.CharField(max_length=30)
    fecha = models.DateTimeField()
    origen = models.DateField()
    destino = models.CharField(max_length=30)
    precio = models.IntegerField()
    sillas_disponibles = models.IntegerField()
