
from django.urls import path, include
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('addStock/', views.addStock, name='addStock'),
    path('buy', views.buy, name="buy"),
    path('buy/<str:prod>/delete', views.delete_prod, name='delete_prod'),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('product/<int:id>', views.product_detail, name="product_detail"),
    path('paypal/', views.paypal, name="paypal"),
    path('preCompra/', views.preCompra, name="preCompra"),
    path('datos/', views.verPedidos, name="verPedidos"),
    path('datos/delete/<int:pedido>', views.eliminarPedido, name="eliminarPedido"),
    path('filtrar/<int:cat>', views.filtrar, name="filtrar"),
    path('state/<int:state>/<int:id>', views.changeState, name="changeState"),
    path('misPedidos/', views.miPedido, name="miPedido"),
    path('pedidoState/<int:id>', views.estadoPedido, name="estadoPedido"),
    path('valorar/<int:id>', views.valorarProducto, name="valorarProducto"),
    path('valorar/<int:mensaje>/delete', views.delete_message, name="delete_message"),
  
]

