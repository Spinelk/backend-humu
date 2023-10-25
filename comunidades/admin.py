from django.contrib import admin
from comunidades.models import *

# admin.site.register(comunidad)


class CanalTextoInline(admin.TabularInline):  # O usa StackedInline si lo prefieres
    model = canalTexto
    extra = 1  # Define el número de formularios en línea que se muestran

class CanalVideoInline(admin.TabularInline):
    model = canalVideo
    extra = 1

@admin.register(comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    inlines = [CanalTextoInline, CanalVideoInline] 