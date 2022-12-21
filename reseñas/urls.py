from django.urls import path, include
from . import views

from django.views.generic import TemplateView
urlpatterns = [

    path('valorar/<int:id>', views.valorarProducto, name="valorarProducto"),
    path('valorar/<int:mensaje>/delete', views.delete_message, name="delete_message"),
]