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

# Se crea una clase que combina los dos formularios creados anteriormente
class BandaYPerfilForm(forms.Form):
    banda = BandaForm()
    perfil_banda = PerfilBandaForm()

