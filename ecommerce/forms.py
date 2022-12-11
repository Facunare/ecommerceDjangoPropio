from django import forms
from django.forms import ModelForm
from .models import stockProducts
class stockForm(ModelForm):
    class Meta:
        model = stockProducts
        fields = ['thumbnail', 'nom_prod', 'precio_prod', 'descripcion', 'categoria']


class preCompra(forms.Form):
    DNI = forms.IntegerField()
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    telefono = forms.IntegerField()
    