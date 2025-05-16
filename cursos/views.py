from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Curso
from .forms import CursoForm

# Create your views here.

@login_required
def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/curso_list.html', {
        'cursos': cursos
    })

@login_required
def curso_create(request):
    if request.method == 'POST':
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso creado exitosamente.')
            return redirect('cursos:list')
    else:
        form = CursoForm()
    
    return render(request, 'cursos/curso_form.html', {
        'form': form,
        'title': 'Crear Curso'
    })

@login_required
def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'cursos/curso_detail.html', {
        'curso': curso
    })

@login_required
def curso_update(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado exitosamente.')
            return redirect('cursos:detail', pk=pk)
    else:
        form = CursoForm(instance=curso)
    
    return render(request, 'cursos/curso_form.html', {
        'form': form,
        'title': 'Editar Curso'
    })

@login_required
def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado exitosamente.')
        return redirect('cursos:list')
    
    return render(request, 'cursos/curso_confirm_delete.html', {
        'curso': curso
    })
