from django.db import models
from django.core.validators import RegexValidator

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(r'^\d{8}$', 'El DNI debe tener 8 dígitos')]
    )
    email = models.EmailField(unique=True)
    telefono = models.CharField(
        max_length=9,
        validators=[RegexValidator(r'^\d{9}$', 'El teléfono debe tener 9 dígitos')]
    )
    fecha_nacimiento = models.DateField()
    carrera = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        ordering = ['apellido', 'nombre']

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"

    def get_nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def get_edad(self):
        from datetime import date
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
