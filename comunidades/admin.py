from django.contrib import admin
from comunidades.models import *

# admin.site.register(comunidad)


class Canal(admin.TabularInline):  # O usa StackedInline si lo prefieres
    model = canal
    extra = 1  # Define el número de formularios en línea que se muestran


@admin.register(comunidad)
class ComunidadAdmin(admin.ModelAdmin):
    inlines = [Canal] 