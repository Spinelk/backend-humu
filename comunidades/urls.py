from django.urls import path
from . import views

urlpatterns = [
    path('obtener_comunidades', views.obtener_comunidades),
    path('crear_comunidad', views.crear_comunidad),
    path('obtener_canales', views.obtener_canales),
]
