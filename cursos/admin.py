from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'creditos', 'docente', 'activo')
    list_filter = ('activo',)
    search_fields = ('codigo', 'nombre', 'docente')
    ordering = ('nombre',)
    fieldsets = (
        ('Información del Curso', {
            'fields': ('codigo', 'nombre', 'creditos')
        }),
        ('Docente', {
            'fields': ('docente',)
        }),
        ('Detalles', {
            'fields': ('descripcion',)
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
