from django import forms


class preCompra(forms.Form):
    DNI = forms.IntegerField()
    nombre = forms.CharField(max_length=60)
    apellido = forms.CharField(max_length=60)
    telefono = forms.IntegerField()
    