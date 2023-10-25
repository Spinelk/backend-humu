from rest_framework import serializers
from .models import comunidad

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = comunidad
        fields = ['id', 'nombre', 'propietario']