from rest_framework import serializers
from .models import *

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = comunidad
        fields = ['id', 'nombre', 'propietario']



class CanalSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = canal
        fields = ['id', 'nombre', 'tipo', 'comunidad']

