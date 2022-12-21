from django.shortcuts import render

from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from productos.models import stockProducts
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import  HttpResponseRedirect
from .models import pedidos, prodsPedidos
from carrito.models import carrito
from ecommerce import models
import operator
from django.db.models import Sum
# Create your views here.

@login_required
def miPedido(request):
    pedido = pedidos.objects.filter(user = request.user)
    return render(request, 'miPedido.html',{
        'pedidos': pedido
    })

@login_required
def estadoPedido(request, id):
    pedido = pedidos.objects.filter(user = request.user).get(pk = id)
    return render(request, 'estadoPedido.html', {
        'pedido': pedido
    })



@staff_member_required
@login_required
def verPedidos(request):
    ventas = pedidos.objects.all()
    totalPedidos = pedidos.objects.all().count()
    totalCliente = User.objects.all().count()
    totalGanancia = 0
    productosDelPedido = prodsPedidos.objects.all()
    for i in ventas:
        totalGanancia += i.total
    return render(request, 'pedidosTotales.html',{
        'pedidos': ventas,
        'total': totalPedidos,
        'totalCliente': totalCliente,
        'ganancia': totalGanancia,
        'productos': productosDelPedido
    })

@login_required
@staff_member_required
def eliminarPedido(request, pedido):
    venta = pedidos.objects.get(pk = pedido)
    if request.method == 'POST':

        venta.delete()
    return redirect('verPedidos')


def changeState(request, state, id):
    pedido = pedidos.objects.get(pk = id)
    if(state==1):
        pedido.estado = 1
    elif(state==2):
        pedido.estado = 2
    elif(state==3):
        pedido.estado = 3
    
    pedido.save()
    return redirect('verPedidos')


def paypal(request):
    total = 0
    prods = carrito.objects.all().filter(user = request.user)
    pedido_id = pedidos.objects.last()
    
    for prod in prods:
        total += prod.precio_prod
    if request.method == "POST":
        pedido = pedidos.objects.create(nombre = request.POST['nombre'] + request.POST['apellido'], DNI = request.POST['DNI'], telefono = request.POST['telefono'], total = total, estado = 0, user= request.user) 
        prods = carrito.objects.all().filter(user = request.user)
        for prod in prods:
            productoStock = stockProducts.objects.get(nom_prod = prod.nom_prod)
            agregado = prodsPedidos.objects.create(pedido_id = pedido, producto_id = productoStock, cantidad = prod.cant_prod)
            prods.delete()
    
        
    return render(request, 'factura.html',{
        'total':total,
        'idPedido': pedido_id,
        'cliente': request.POST['nombre'] + " " + request.POST['apellido'],
        'productos': prodsPedidos.objects.all(),
        
    })
    
