from rest_framework import serializers
from .models import *

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = comunidad
        fields = ['id', 'nombre', 'propietario']



class CanalTextoSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = canalTexto
        fields = ['id', 'nombre', 'comunidad']

class CanalVideoSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = canalVideo
        fields = ['id', 'nombre', 'comunidad']