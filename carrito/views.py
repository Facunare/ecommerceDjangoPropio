
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import  HttpResponseRedirect
from .models import carrito, stockProducts

from ecommerce import models
import operator
from django.db.models import Sum

# Create your views here.

@login_required
def addCart(request, prod):
    ArrayProductos = []
    cantidad = request.GET.get("cant")


    product = get_object_or_404(stockProducts, nom_prod=prod)
    products = carrito.objects.all().filter(user = request.user)

    for i in products:
        ArrayProductos.append(i.nom_prod)

    if cantidad:
        if product.nom_prod in ArrayProductos:
            p = carrito.objects.filter(user = request.user).get(nom_prod=prod)
            p.cant_prod += int(cantidad)
            p.precio_prod += p.precio_prod*int(cantidad)
            p.save()
        else:
            carrito.objects.create(foto = product.thumbnail, nom_prod = product.nom_prod, cant_prod=int(cantidad), precio_prod = product.precio_prod*int(cantidad), prod = product,  user = request.user)
       
    else:
        return render(request, "product_detail.html",{
            'data':product,
            'error': 'No se eligio una cantidad'
        })    
    
    return redirect('cart')



@login_required
def cart(request):
    total = 0
    prods = carrito.objects.all().filter(user = request.user)
    for prod in prods:
        total += prod.precio_prod
    
    
    return render(request, 'addToCart.html',{
        'prods': prods,
        'total': total
    })

    
@login_required 
def deleteFromCart(request, prod):
 
    product = carrito.objects.filter(user = request.user).get(nom_prod=prod)
    if request.method == 'POST':
        product.delete()
        return redirect('cart')

        

@staff_member_required
def update_stock(request, prod):
    product = get_object_or_404(stockProducts, nom_prod=prod)

    product.hayStock = operator.not_(product.hayStock)
    product.save()
    

    return redirect('buy')

@login_required
def delete_all(request):
    prods = carrito.objects.all().filter(user = request.user)
    if request.method == 'POST':
        prods.delete()
        return redirect('cart')