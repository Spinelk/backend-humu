from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class comunidad(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    propietario = models.ForeignKey(
        'usuarios.perfil', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



class canalTexto(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    comunidad = models.ForeignKey(comunidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class canalVideo(models.Model):
    nombre = models.CharField(max_length=100, blank=True, null=True)
    comunidad = models.ForeignKey(comunidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre



@receiver(post_save, sender=comunidad)
def crear_canales_por_defecto(sender, instance, created, **kwargs):
    if created:
        nombre_canal_texto = f"Canal de Texto de {instance.nombre}"
        nombre_canal_video = f"Canal de Video de {instance.nombre}"
        canalTexto.objects.create(nombre=nombre_canal_texto, comunidad=instance)
        canalVideo.objects.create(nombre=nombre_canal_video, comunidad=instance)