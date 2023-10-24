from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User as usuario
from django.contrib.auth import login, authenticate, logout

from .serializers import UserSerializer

from django.middleware.csrf import get_token

from django.contrib.auth.decorators import login_required

from usuarios.models import perfil

# registrar usuario con nombre de usuario, correo y contraseña
@api_view(['POST'])
def registrar_usuario(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        nombreUsuario = request.data['nombreUsuario']
        contrasena = request.data['contrasena']
        verificadorContrasena = request.data['verificadorContrasena']
        
        # verificar que las contraseñas coincidan
        if contrasena != verificadorContrasena:
            return Response({'mensaje': 'Las contraseñas no coinciden'}, status=status.HTTP_400_BAD_REQUEST)

        user = usuario.objects.get(username=nombreUsuario)
        user.set_password(contrasena)
        user.save()
        perfil.objects.create(usuario=user)
        # Autenticar al usuario después del registro
        login(request, user)
        return Response({'mensaje': 'Registro exitoso'})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# iniciar sesion con nombre de usuario y contraseña
@api_view(['POST'])
def iniciar_sesion(request):
    nombreUsuario = request.data['nombreUsuario']
    contrasena = request.data['contrasena']
    usuario = authenticate(request, username=nombreUsuario, password=contrasena)
    if usuario is not None:
        login(request, usuario)
        serializer = UserSerializer(usuario)
        return Response({'usuario': usuario.username, 'correo': usuario.email})
    else:
        return Response({'mensaje': 'Credenciales inválidas'}, status=status.HTTP_401_UNAUTHORIZED)


# verificar token de autenticación
@api_view(['GET'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def test_session(request):
    return Response("Sesión válida!")


# eliminar usuario con nombre de usuario y contraseña
@api_view(['DELETE'])
@authentication_classes([SessionAuthentication])
# @permission_classes([IsAuthenticated])
def eliminar_usuario(request):
    usuario = get_object_or_404(usuario, username=request.data['nombreUsuario'])
    if not usuario.check_password(request.data['contrasena']):
        return Response("La contraseña no es valida", status=status.HTTP_400_BAD_REQUEST)
    usuario.delete()
    return Response("usuario eliminado", status=status.HTTP_200_OK)


# obtener información del usuario
@login_required
def obtener_informacion_usuario(request):
    usuario = request.usuario
    data = {
        'nombre': usuario.first_name,
        'apellido': usuario.last_name,
        'email': usuario.email,
        # Agrega más datos según sea necesario
    }
    return JsonResponse(data)


# cerrar sesión
@api_view(['POST'])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def cerrar_sesion(request):
    logout(request)
    return Response("Sesión cerrada", status=status.HTTP_200_OK)


# obtener token csrf
def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})