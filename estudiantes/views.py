from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Estudiante
from .forms import EstudianteForm
from cursos.models import Curso
from matriculas.models import Matricula
from notas.models import Nota

# Create your views here.

@login_required
def estudiante_list(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/estudiante_list.html', {
        'estudiantes': estudiantes
    })

@login_required
def estudiante_create(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante creado exitosamente.')
            return redirect('estudiantes:list')
    else:
        form = EstudianteForm()
    
    return render(request, 'estudiantes/estudiante_form.html', {
        'form': form,
        'title': 'Crear Estudiante'
    })

@login_required
def estudiante_detail(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    return render(request, 'estudiantes/estudiante_detail.html', {
        'estudiante': estudiante
    })

@login_required
def estudiante_update(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estudiante actualizado exitosamente.')
            return redirect('estudiantes:detail', pk=pk)
    else:
        form = EstudianteForm(instance=estudiante)
    
    return render(request, 'estudiantes/estudiante_form.html', {
        'form': form,
        'title': 'Editar Estudiante'
    })

@login_required
def estudiante_delete(request, pk):
    try:
        estudiante = get_object_or_404(Estudiante, pk=pk)
        if request.method == 'POST':
            estudiante.delete()
            messages.success(request, 'Estudiante eliminado exitosamente.')
            return redirect('estudiantes:list')
        
        return render(request, 'estudiantes/estudiante_confirm_delete.html', {
            'estudiante': estudiante
        })
    except Exception as e:
        messages.error(request, f'Error al eliminar el estudiante: {str(e)}')
        return redirect('estudiantes:list')

@login_required
def dashboard(request):
    try:
        total_estudiantes = Estudiante.objects.count()
        total_cursos = Curso.objects.count()
        total_matriculas = Matricula.objects.count()
        total_notas = Nota.objects.count()
        
        context = {
            'total_estudiantes': total_estudiantes,
            'total_cursos': total_cursos,
            'total_matriculas': total_matriculas,
            'total_notas': total_notas,
        }
        return render(request, 'dashboard.html', context)
    except Exception as e:
        messages.error(request, f'Error al cargar el dashboard: {str(e)}')
        return render(request, 'dashboard.html', {
            'total_estudiantes': 0,
            'total_cursos': 0,
            'total_matriculas': 0,
            'total_notas': 0,
        })
