from django import forms
from cms.models import pais

class PaisForm(forms.ModelForm):
    class Meta:
        model =  pais
        fields = ['codigo', 'nombre', 'nacionalidad', 'moneda']
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
            'moneda': forms.TextInput(attrs={'class': 'form-control'}),            
        }