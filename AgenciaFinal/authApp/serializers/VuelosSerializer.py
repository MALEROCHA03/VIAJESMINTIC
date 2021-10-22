from authApp.models.Vuelos import Vuelos
from rest_framework import serializers


class VuelosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vuelos
        fields = ['IdVuelo', 'aerolinea', 'fecha', 'origen', 'destino', 'precio',
                  'sillas_disponibles']
