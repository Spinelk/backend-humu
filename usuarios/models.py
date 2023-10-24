from django.db import models
from django.contrib.auth.models import User as usuario

class perfil(models.Model):
    usuario = models.OneToOneField(usuario, on_delete=models.CASCADE)
    test = models.CharField(max_length=100, blank=True, null=True, default='test')

    def __str__(self):
        return self.usuario.username