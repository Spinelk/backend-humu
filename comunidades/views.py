from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication

from .serializers import *
from .models import *

# Create your views here.


@api_view(['POST'])
def crear_comunidad(request):
    nombre = request.data['nombre']
    propietario = request.data['propietario']
    print(nombre)
    print(propietario)
    return Response({'mensaje': 'Registro exitoso'})


@api_view(['GET'])
def obtener_comunidades(request):
    comunidades = comunidad.objects.all()
    serializer = ComunidadSerializer(comunidades, many=True)
    return Response(serializer.data)

# Obtener todos los caneles de una comunidad
@api_view(['POST'])
def obtener_canales(request):
    comunidad_id = request.data['comunidad_id']
    canales = canal.objects.filter(comunidad=comunidad_id)
    serializer = CanalSerializer(canales, many=True)
    return Response(serializer.data)
