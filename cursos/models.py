from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nombre']

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    def get_total_estudiantes(self):
        return self.matricula_set.count()

    def get_promedio_notas(self):
        from notas.models import Nota
        notas = Nota.objects.filter(curso=self)
        if notas.exists():
            return sum(nota.valor for nota in notas) / notas.count()
        return 0
