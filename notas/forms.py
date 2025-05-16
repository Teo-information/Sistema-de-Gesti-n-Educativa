from django import forms
from .models import Nota

class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['estudiante', 'curso', 'valor', 'observaciones']
        widgets = {
            'estudiante': forms.Select(attrs={'class': 'form-control'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 20, 'step': 0.1}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        } 