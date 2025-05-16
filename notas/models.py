from django.db import models
from estudiantes.models import Estudiante
from cursos.models import Curso

class Nota(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=4, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    observaciones = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Nota'
        verbose_name_plural = 'Notas'
        unique_together = ['estudiante', 'curso']
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"{self.estudiante} - {self.curso}: {self.valor}"

    def get_estado(self):
        return 'APROBADO' if self.valor >= 11 else 'DESAPROBADO'

    def save(self, *args, **kwargs):
        # Validar que el valor esté entre 0 y 20
        if self.valor < 0 or self.valor > 20:
            raise ValueError('La nota debe estar entre 0 y 20')
        super().save(*args, **kwargs)
