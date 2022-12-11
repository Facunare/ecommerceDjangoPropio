from django import forms
from django.forms import ModelForm

class FormularioContacto(forms.Form):
    asunto=forms.CharField(max_length=70)
    mensaje=forms.CharField(max_length=500)
    email=forms.EmailField()