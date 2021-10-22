from django.db import models
from .user import Usuarios
from .Vuelos import Vuelos


class Reserva(models.Model):
    idReserva = models.AutoField(primary_key=True)
    idUsuario = models.ForeignKey(Usuarios, related_name='idViajero', on_delete=models.CASCADE)
    numero_vuelo = models.ForeignKey(Vuelos, related_name='numero_vuelo', on_delete=models.CASCADE)
