from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import  HttpResponseRedirect
from .models import valoraciones
from productos.models import stockProducts
from ecommerce import models
import operator
from django.db.models import Sum

# Create your views here.

@login_required
def valorarProducto(request, id):

    product = get_object_or_404(stockProducts, pk = id)
    if request.method == "POST":
        next = request.POST.get('next', '/')
        

        valoraciones.objects.create(producto = product, estrellas = request.POST["estrellas"], mensaje = request.POST["mensaje"], user = request.user)
        return HttpResponseRedirect(next)


@login_required
@staff_member_required
def delete_message(request, mensaje):
    msg = valoraciones.objects.get(pk = mensaje)
    if request.method == 'POST':
        next = request.POST.get('next1', '/')
        msg.delete()
    return HttpResponseRedirect(next)
