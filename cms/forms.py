from django import forms
from cms.models import pais, region, provincia, comuna, empresa, representante, colegio
from django import forms

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


class RegionForm(forms.ModelForm):
    class Meta:
        model =  region
        fields = ['pais','codigo', 'nombre']
        widgets = {
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProvinciaForm(forms.ModelForm):
    class Meta:
        model =  provincia
        fields = ['region','codigo', 'nombre']
        widgets = {
            'region': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ComunaForm(forms.ModelForm):
    class Meta:
        model =  comuna
        fields = ['provincia','codigo', 'nombre']
        widgets = {
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model =  empresa
        fields = ['rut', 'razonsocial', 'comuna', 'direccion', 'telefono', 'email', 'logo']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'razonsocial': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),            
        }

class RepresentanteForm(forms.ModelForm):
    class Meta:
        model =  representante
        fields = ['empresa', 'rut', 'nombre', 'apellido', 'email', 'telefono', 'comunas', 'direccion']
        widgets = {
            'empresa': forms.Select(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'comunas': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

class ColegioForm(forms.ModelForm):
    class Meta:
        model =  colegio
        fields = ['razon_social', 'comuna', 'direccion', 'telefono', 'email']
        widgets = {
            'razon_social': forms.TextInput(attrs={'class': 'form-control'}),
            'comuna': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }

