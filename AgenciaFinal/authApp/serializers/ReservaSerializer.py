from authApp.models.reserva import Reserva
from rest_framework import serializers


class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['idReserva', 'idUsuario', 'numero_vuelo']
