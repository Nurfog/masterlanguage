from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import PaisForm

@login_required
@csrf_exempt
def crear_pais(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_paises')
    else: 
        form = PaisForm()
    return render(request, 'pages/crear_pais.html', {'form': form})


def lista_paises(request):
    paises = pais.objects.all()
    return render(request, 'pages/lista_paises.html', {'paises': paises})