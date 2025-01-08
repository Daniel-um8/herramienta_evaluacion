from django import forms
from .models import Banda, PerfilBanda

class PerfilBandaForm(forms.ModelForm):
    class Meta:
        model = PerfilBanda
        fields = ['descripcion', 'anio_formacion', 'genero']

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ['nombre']

# Crearemos un formulario comnbinado para crear una banda y su perfil al mismo tiempo.
# class BandaPerfilForm(forms.ModelForm):
#     class Meta:
#         model = Banda
#         fields = ['nombre']

#     descripcion = forms.CharField(max_length=200)
#     anio_formacion = forms.IntegerField()
#     genero = forms.CharField(max_length=100)

class BandaYPerfilForm(forms.Form):
    banda = BandaForm()
    perfil_banda = PerfilBandaForm()
