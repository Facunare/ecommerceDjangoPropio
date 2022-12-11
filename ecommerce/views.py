
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import  HttpResponseRedirect
from .models import stockProducts,  pedidos, categorias, valoraciones, productoPedido
from . import forms
from ecommerce import models
import operator
from django.db.models import Sum

# 1. Diseño.

# 2. Mercado pago.

# 4. Mostrar productos del pedido.

# 5. Mostrar factura a cliente.

# 6. Dividir proyecto en aplicaciones.

# 7. Crear funciones internas en la base de datos.

def paypal(request):
    total = 0
    prods = carrito.objects.all().filter(user = request.user)
   
    for prod in prods:
        total += prod.precio_prod
    if request.method == "POST":
        pedidos.objects.create(nombre = request.POST['nombre'] + request.POST['apellido'], DNI = request.POST['DNI'], telefono = request.POST['telefono'], total = total, estado = 0, user= request.user) 
        # carro = carrito.objects.all().filter(user = request.user)
        # productos_pedidos = list()

        # for prod in carro:
        #     productos_pedidos.append(productoPedido(
        #         cantidad = value['cantidad'],
        #         user = request.user,
        #         producto_id = key,
        #         pedido_id = pedido
        #     ))
        
        # productoPedido.objects.bulk_create(productos_pedidos)
        

        prods.delete()
    # return render(request, 'paypal.html',{
    #     'total':total
    # })
    return redirect('factura')

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
        
   




def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')
    
@login_required
def addStock(request):
  
    if request.method == 'GET':
        return render(request, 'addProduct.html', {
            'form' : forms.stockForm
        })
    else:
        print(request.POST)
        print(models.categorias.objects.get(id=request.POST['categoria']))

        stockProducts.objects.create(thumbnail = request.FILES['thumbnail'], nom_prod=request.POST['nom_prod'], precio_prod=request.POST['precio_prod'], descripcion=request.POST['descripcion'],
        categoria=models.categorias.objects.get(id=request.POST['categoria']))

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

    
@login_required
def preCompra(request):
    form = forms.preCompra
    return render(request, 'preCompra.html',{
        'form': form
    })


@staff_member_required
@login_required
def verPedidos(request):
    ventas = pedidos.objects.all()
    totalPedidos = pedidos.objects.all().count()
    totalCliente = User.objects.all().count()
    totalGanancia = 0
    for i in ventas:
        totalGanancia += i.total
    return render(request, 'pedidosTotales.html',{
        'pedidos': ventas,
        'total': totalPedidos,
        'totalCliente': totalCliente,
        'ganancia': totalGanancia
    })

@login_required
@staff_member_required
def eliminarPedido(request, pedido):
    venta = pedidos.objects.get(pk = pedido)
    if request.method == 'POST':

        venta.delete()
    return redirect('verPedidos')

@login_required
def delete_all(request):
    prods = carrito.objects.all().filter(user = request.user)
    if request.method == 'POST':
        prods.delete()
        return redirect('cart')

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
