from django.contrib import admin
from .models import Estudiante

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'apellido', 'nombre', 'carrera', 'email', 'activo')
    list_filter = ('carrera', 'activo')
    search_fields = ('dni', 'apellido', 'nombre', 'email')
    ordering = ('apellido', 'nombre')
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'apellido', 'dni', 'fecha_nacimiento')
        }),
        ('Contacto', {
            'fields': ('email', 'telefono')
        }),
        ('Información Académica', {
            'fields': ('carrera',)
        }),
        ('Estado', {
            'fields': ('activo',)
        }),
    )
