from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Nota
from .forms import NotaForm

# Create your views here.

@login_required
def nota_list(request):
    notas = Nota.objects.all().select_related('estudiante', 'curso')
    return render(request, 'notas/nota_list.html', {'notas': notas})

@login_required
def nota_create(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota creada exitosamente.')
            return redirect('notas:list')
    else:
        form = NotaForm()
    
    return render(request, 'notas/nota_form.html', {
        'form': form,
        'title': 'Crear Nota'
    })

@login_required
def nota_detail(request, pk):
    nota = get_object_or_404(Nota.objects.select_related('estudiante', 'curso'), pk=pk)
    return render(request, 'notas/nota_detail.html', {
        'nota': nota
    })

@login_required
def nota_update(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota actualizada exitosamente.')
            return redirect('notas:list')
    else:
        form = NotaForm(instance=nota)
    
    return render(request, 'notas/nota_form.html', {
        'form': form,
        'title': 'Editar Nota'
    })

@login_required
def nota_delete(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        messages.success(request, 'Nota eliminada exitosamente.')
        return redirect('notas:list')
    
    return render(request, 'notas/nota_confirm_delete.html', {
        'nota': nota
    })
