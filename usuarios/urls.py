from django.urls import path
from . import views

urlpatterns = [
    path('registrar_usuario', views.registrar_usuario),
    path('iniciar_sesion', views.iniciar_sesion),
    path('test_session', views.test_session),
    path('eliminar_usuario', views.eliminar_usuario),
    path('get_csrf_token', views.get_csrf_token),
]
