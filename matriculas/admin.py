from django.contrib import admin
from .models import Matricula

@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'curso', 'fecha_matricula', 'estado')
    list_filter = ('estado', 'fecha_matricula')
    search_fields = ('estudiante__apellido', 'estudiante__nombre', 'curso__nombre')
    ordering = ('-fecha_matricula',)
    fieldsets = (
        ('Información de Matrícula', {
            'fields': ('estudiante', 'curso')
        }),
        ('Estado', {
            'fields': ('estado',)
        }),
    )
