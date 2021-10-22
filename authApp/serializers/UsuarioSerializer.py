from authApp.models.user import Usuarios
from rest_framework import serializers


class ViajeroSerializer(serializers.ModelSerializer):
    # Create your views here.
    class Meta:
        model = Usuarios
        fields = ['id', 'password', 'rol', 'nombre', 'apellidos', 'email', 'estado', 'telefono_viajero']

    def to_representation(self, obj):
        user = Usuarios.objects.get(id=obj.id)
        return {
            'id': user.id,
            'password': user.password,
            'rol': user.rol,
            'nombre': user.nombre,
            'apellidos': user.apellidos,
            'email': user.email,
            'estado': user.estado,
            'telefono_viajero': user.telefono_viajero,
        }
