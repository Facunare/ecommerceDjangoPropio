from django.urls import path, include
from . import views

from django.views.generic import TemplateView

urlpatterns = [

    path('addStock/', views.addStock, name='addStock'),
    path('buy', views.buy, name="buy"),
    path('filtrar/<int:cat>', views.filtrar, name="filtrar"),
    path('buy/<str:prod>/delete', views.delete_prod, name='delete_prod'),
    path('product/<int:id>', views.product_detail, name="product_detail"),
]