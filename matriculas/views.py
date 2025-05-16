from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Matricula
from .forms import MatriculaForm
from notas.models import Nota

# Create your views here.

@login_required
def matricula_list(request):
    matriculas = Matricula.objects.all().select_related('estudiante', 'curso')
    # Prefetch las notas para cada matrícula
    notas = Nota.objects.filter(
        estudiante__in=[m.estudiante for m in matriculas],
        curso__in=[m.curso for m in matriculas]
    )
    # Crear un diccionario para acceso rápido a las notas
    nota_dict = {(n.estudiante_id, n.curso_id): n for n in notas}
    # Asignar las notas a las matrículas
    for matricula in matriculas:
        matricula.nota = nota_dict.get((matricula.estudiante_id, matricula.curso_id))
    return render(request, 'matriculas/matricula_list.html', {'matriculas': matriculas})

@login_required
def matricula_create(request):
    if request.method == 'POST':
        form = MatriculaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Matrícula creada exitosamente.')
            return redirect('matriculas:list')
    else:
        form = MatriculaForm()
    
    return render(request, 'matriculas/matricula_form.html', {
        'form': form,
        'title': 'Crear Matrícula'
    })

@login_required
def matricula_detail(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)
    nota = Nota.objects.filter(estudiante=matricula.estudiante, curso=matricula.curso).first()
    return render(request, 'matriculas/matricula_detail.html', {
        'matricula': matricula,
        'nota': nota
    })

@login_required
def matricula_update(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)
    if request.method == 'POST':
        form = MatriculaForm(request.POST, instance=matricula)
        if form.is_valid():
            form.save()
            messages.success(request, 'Matrícula actualizada exitosamente.')
            return redirect('matriculas:list')
    else:
        form = MatriculaForm(instance=matricula)
    
    return render(request, 'matriculas/matricula_form.html', {
        'form': form,
        'title': 'Editar Matrícula'
    })

@login_required
def matricula_delete(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)
    if request.method == 'POST':
        matricula.delete()
        messages.success(request, 'Matrícula eliminada exitosamente.')
        return redirect('matriculas:list')
    
    return render(request, 'matriculas/matricula_confirm_delete.html', {
        'matricula': matricula
    })
