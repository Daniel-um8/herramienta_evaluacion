from django.shortcuts import render, redirect
# Imports para formulario combinado (anidado)
from .forms import BandaForm, PerfilBandaForm
from .models import Banda

def index(request):
    return render(request, 'app1/index.html')  # Renderizar la vista index.html con la información necesaria.

# Formulario combinado (anidado)
def crear_banda_con_perfil(request):
    if request.method == 'POST':
        banda_form = BandaForm(request.POST)
        perfil_form = PerfilBandaForm(request.POST)

        if banda_form.is_valid() and perfil_form.is_valid():
            # Primero guardamos el perfil
            perfil_banda = perfil_form.save()
            # Luego creamos la banda y asignamos el perfil
            banda = banda_form.save(commit=False)
            banda.perfil = perfil_banda
            banda.save()

            return redirect('index')  # Redirigir a una página de éxito

    else:
        banda_form = BandaForm()
        perfil_form = PerfilBandaForm()

    return render(request, 'app1/crear_banda.html', {'banda_form': banda_form,'perfil_form': perfil_form,})

# LISTAR BANDAS
def listar_bandas(request):
    bandas = Banda.objects.all()
    return render(request, 'app1/listar_bandas.html', {'bandas': bandas})

