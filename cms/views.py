from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from .forms import *

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

@login_required
@csrf_exempt
def editar_pais(request, id):
    paix = pais.objects.get(id=id)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=paix)
        if form.is_valid():
            #guardar los datos en la base de datos en mayuscula
            form.codigo = form.cleaned_data['codigo'].upper()
            form.nombre = form.cleaned_data['nombre'].upper()
            form.nacionalidad = form.cleaned_data['nacionalidad'].upper()
            form.moneda = form.cleaned_data['moneda'].upper()
            form.save()
            #form.save(commit=False)

            return redirect('lista_paises')
    else:
        form = PaisForm(instance=paix)
    return render(request, 'pages/editar_pais.html', {'form': form, 'pais': paix})

@login_required
@csrf_exempt
def eliminar_pais(request, id):
    paix = pais.objects.get(id=id)
    paix.delete()
    return redirect('lista_paises')

@login_required
@csrf_exempt
def crear_region(request):
    if request.method == 'POST':
        form = RegionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_region')
    else: 
        form = RegionForm()
    return render(request, 'pages/crear_region.html', {'form': form})


def lista_region(request):
    regiones = region.objects.all()
    return render(request, 'pages/lista_region.html', {'regiones': regiones})

@login_required
@csrf_exempt
def editar_region(request, id):
    region = region.objects.get(id=id)
    if request.method == 'POST':
        form = RegionForm(request.POST, instance=region)
        if form.is_valid():
            form.save()
            return redirect('lista_region')
    else:
        form = RegionForm(instance=region)
    return render(request, 'pages/editar_region.html', {'form': form, 'region': region})

@login_required
@csrf_exempt
def eliminar_region(request, id):
    region = region.objects.get(id=id)
    region.delete()
    return redirect('lista_region')

@login_required
@csrf_exempt
def crear_provincia(request):
    if request.method == 'POST':
        form = ProvinciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_provincia')
    else: 
        form = ProvinciaForm()
    return render(request, 'pages/crear_provincia.html', {'form': form})

def lista_provincia(request):
    provincias = provincia.objects.all()
    return render(request, 'pages/lista_provincia.html', {'provincias': provincias})

@login_required
@csrf_exempt
def editar_provincia(request, id):
    provincia = provincia.objects.get(id=id)
    if request.method == 'POST':
        form = ProvinciaForm(request.POST, instance=provincia)
        if form.is_valid():
            form.save()
            return redirect('lista_provincia')
    else:
        form = ProvinciaForm(instance=provincia)
    return render(request, 'pages/editar_provincia.html', {'form': form, 'provincia': provincia})

@login_required
@csrf_exempt
def eliminar_provincia(request, id):
    provincia = provincia.objects.get(id=id)
    provincia.delete()
    return redirect('lista_provincia')

@login_required
@csrf_exempt
def crear_comuna(request):
    if request.method == 'POST':
        form = ComunaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_comuna')
    else: 
        form = ComunaForm()
    return render(request, 'pages/crear_comuna.html', {'form': form})

def lista_comunas(request):
    comunas = comuna.objects.all()
    return render(request, 'pages/lista_comuna.html', {'comunas': comunas})

@login_required
@csrf_exempt
def editar_comuna(request, id):
    comuna = comuna.objects.get(id=id)
    if request.method == 'POST':
        form = ComunaForm(request.POST, instance=comuna)
        if form.is_valid():
            form.save()
            return redirect('lista_comuna')
    else:
        form = ComunaForm(instance=comuna)
    return render(request, 'pages/editar_comuna.html', {'form': form, 'comuna': comuna})

@login_required
@csrf_exempt
def eliminar_comuna(request, id):
    comuna = comuna.objects.get(id=id)
    comuna.delete()
    return redirect('lista_comuna')

@login_required
@csrf_exempt
def crear_empresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empresa')
    else: 
        form = EmpresaForm()
    return render(request, 'pages/crear_empresa.html', {'form': form})

def lista_empresa(request):
    empresas = empresa.objects.all()
    return render(request, 'pages/lista_empresa.html', {'empresas': empresas})

@login_required
@csrf_exempt
def editar_empresa(request, id):
    empresa = empresa.objects.get(id=id)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('lista_empresa')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'pages/editar_empresa.html', {'form': form, 'empresa': empresa})

@login_required
@csrf_exempt
def eliminar_empresa(request, id):
    empresa = empresa.objects.get(id=id)
    empresa.delete()
    return redirect('lista_empresa')

@login_required
@csrf_exempt
def crear_representante(request):
    if request.method == 'POST':
        form = RepresentanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_representante')
    else: 
        form = RepresentanteForm()
    return render(request, 'pages/crear_representante.html', {'form': form})

def lista_representante(request):
    representantes = representante.objects.all()
    return render(request, 'pages/lista_representante.html', {'representantes': representantes})    

@login_required
@csrf_exempt
def editar_representante(request, id):
    representante = representante.objects.get(id=id)
    if request.method == 'POST':
        form = RepresentanteForm(request.POST, instance=representante)
        if form.is_valid():
            form.save()
            return redirect('lista_representante')
    else:
        form = RepresentanteForm(instance=representante)
    return render(request, 'pages/editar_representante.html', {'form': form, 'representante': representante})

@login_required
@csrf_exempt
def eliminar_representante(request, id):
    representante = representante.objects.get(id=id)
    representante.delete()
    return redirect('lista_representante')

@login_required
@csrf_exempt
def crear_colegio(request):
    if request.method == 'POST':
        form = ColegioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_colegio')
    else: 
        form = ColegioForm()
    return render(request, 'pages/crear_colegio.html', {'form': form})

def lista_colegio(request):
    colegios = colegio.objects.all()
    return render(request, 'pages/lista_colegio.html', {'colegios': colegios})

@login_required
@csrf_exempt
def editar_colegio(request, id):
    colegio = colegio.objects.get(id=id)
    if request.method == 'POST':
        form = ColegioForm(request.POST, instance=colegio)
        if form.is_valid():
            form.save()
            return redirect('lista_colegio')
    else:
        form = ColegioForm(instance=colegio)
    return render(request, 'pages/editar_colegio.html', {'form': form, 'colegio': colegio})

@login_required
@csrf_exempt
def eliminar_colegio(request, id):
    colegio = colegio.objects.get(id=id)
    colegio.delete()
    return redirect('lista_colegio')





