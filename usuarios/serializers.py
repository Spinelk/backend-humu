from rest_framework import serializers
from django.contrib.auth.models import User as usuario

class UserSerializer(serializers.ModelSerializer):
    nombreUsuario = serializers.CharField(source='username')
    contrasena = serializers.CharField(source='password')
    correo = serializers.EmailField(source='email')

    class Meta(object):
        model = usuario
        fields = ['id', 'nombreUsuario', 'contrasena', 'correo']