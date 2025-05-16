from django.contrib import admin
from .models import Nota

@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'valor', 'fecha_registro', 'get_estado')
    list_filter = ('fecha_registro', 'curso')
    search_fields = ('estudiante__apellido', 'estudiante__nombre', 'curso__nombre')
    ordering = ('-fecha_registro',)
    fieldsets = (
        ('Información de la Nota', {
            'fields': ('estudiante', 'curso', 'valor')
        }),
        ('Detalles', {
            'fields': ('observaciones',)
        }),
    )

    def get_estado(self, obj):
        return obj.get_estado()
    get_estado.short_description = 'Estado'
