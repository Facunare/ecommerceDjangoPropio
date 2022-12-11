from django.shortcuts import render
from . import forms
from django.core.mail import send_mail
# Create your views here.
def contacto(request):
    
    if request.method=="POST":
        
        miFormulario=forms.FormularioContacto(request.POST)

        if miFormulario.is_valid():
            inForm=miFormulario.cleaned_data
            print(inForm)
            send_mail(inForm['asunto'], inForm['mensaje'], inForm.get('email', ''), ['davidarechagaippolito@gmail.com'],)

            return render(request, "formulario_contacto.html")
    else:

        miFormulario=forms.FormularioContacto()

    
    
    return render(request, "formulario_contacto.html", {"form":miFormulario})