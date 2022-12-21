
from django.urls import path, include
from . import views

from django.views.generic import TemplateView

urlpatterns = [

    
    path('datos/', views.verPedidos, name="verPedidos"),
    path('datos/delete/<int:pedido>', views.eliminarPedido, name="eliminarPedido"),
    path('paypal/', views.paypal, name="paypal"),
    path('state/<int:state>/<int:id>', views.changeState, name="changeState"),
    path('misPedidos/', views.miPedido, name="miPedido"),
    path('pedidoState/<int:id>', views.estadoPedido, name="estadoPedido"),
]


