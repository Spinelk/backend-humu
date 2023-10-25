from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ComunidadSerializer
from .models import comunidad

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