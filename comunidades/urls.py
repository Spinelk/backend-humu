from django.urls import path
from . import views

urlpatterns = [
    path('obtener_comunidades', views.obtener_comunidades),
]
