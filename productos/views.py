from django.shortcuts import render

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import  HttpResponseRedirect
from carrito.models import carrito
from ecommerce import models
import operator
from django.db.models import Sum
from .models import stockProducts
from . import forms
from reseñas.models import valoraciones
from categoria.models import categorias
# from categoria.models import categorias


# Create your views here.
@login_required
def addStock(request):
  
    if request.method == 'GET':
        return render(request, 'addProduct.html', {
            'form' : forms.stockForm
        })
    else:
        stockProducts.objects.create(thumbnail = request.FILES['thumbnail'], nom_prod=request.POST['nom_prod'], precio_prod=request.POST['precio_prod'], descripcion=request.POST['descripcion'],
        categoria=categorias.objects.get(id=request.POST['categoria']))

        return redirect('buy')
    


@login_required
def buy(request):
    busqueda = request.GET.get("buscar")
      
    stock = stockProducts.objects.all()
    categoria = categorias.objects.all()

    if busqueda:
        stock = stockProducts.objects.filter(
            nom_prod__icontains = busqueda
        )
    
    return render(request, 'buy.html', {
        'products' : stock,
        'categorias':categoria
    })

@login_required 
@staff_member_required
def delete_prod(request, prod):
    
    product = get_object_or_404(stockProducts, nom_prod=prod)
    if request.method == 'POST':
        
        product.delete()
        return redirect('buy')

@login_required
def filtrar(request, cat):
    tipo = categorias.objects.get(pk=cat)
    cats = categorias.objects.all()
    
    stock = stockProducts.objects.filter(
        categoria = tipo
    )
    
    return render(request, 'buy.html', {
        'products' : stock,
        'categorias':cats,
    })


@login_required
def product_detail(request, id):
    if request.method == 'GET':
        product = stockProducts.objects.get(pk=id)
        form = forms.stockForm(instance=product)
        reseñas = valoraciones.objects.all().filter(producto_id=id)
        cantidadEstrellas = valoraciones.objects.filter(producto_id = id).aggregate(Sum('estrellas'))
        cantidadReseñas = valoraciones.objects.filter(producto_id = id).count()
        print(cantidadReseñas)
        print(cantidadEstrellas)
        promedio = cantidadEstrellas['estrellas__sum'] / cantidadReseñas
        print(reseñas)
        return render(request, 'product_detail.html',{
            'data': product,
            'form': form,
            'valoraciones': reseñas,
            'reseñasTotales': cantidadReseñas,
            'promedio': promedio
        })
    else:
        try:
            product = stockProducts.objects.get(pk=id)
            form = forms.stockForm(request.POST, instance=product)
            form.save()
            return redirect('buy')
        except ValueError:
            return render(request, 'product_detail.html',{
                'data': product,
                'form': form,
                'error': 'Error actualizando el producto'
            })
