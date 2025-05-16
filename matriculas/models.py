from django.db import models
from estudiantes.models import Estudiante
from cursos.models import Curso

class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_matricula = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[
            ('ACTIVA', 'Activa'),
            ('RETIRADA', 'Retirada'),
            ('COMPLETADA', 'Completada')
        ],
        default='ACTIVA'
    )

    class Meta:
        verbose_name = 'Matrícula'
        verbose_name_plural = 'Matrículas'
        unique_together = ['estudiante', 'curso']
        ordering = ['-fecha_matricula']

    def __str__(self):
        return f"{self.estudiante} - {self.curso}"

    def get_estado_nota(self):
        from notas.models import Nota
        nota = Nota.objects.filter(estudiante=self.estudiante, curso=self.curso).first()
        if nota:
            return 'APROBADO' if nota.valor >= 11 else 'DESAPROBADO'
        return 'PENDIENTE'
