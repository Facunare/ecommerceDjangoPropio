from django.urls import path, include
from . import views

from django.views.generic import TemplateView
urlpatterns = [

    path('cart/', views.cart, name="cart"),
    path('cart/delete_all', views.delete_all, name="delete_all"),
    path('cart/<str:prod>', views.addCart, name="addCart"),
    path('cart/delete/<str:prod>', views.deleteFromCart, name="deleteFromCart"),
    path('cart/update/<str:prod>', views.update_stock, name="update_stock"),
]