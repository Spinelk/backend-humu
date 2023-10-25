from django.db import models

class comunidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    propietario = models.ForeignKey('usuarios.perfil', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre