from django.db import models
from django.contrib.auth.models import User
from carrito.models import carrito
from productos.models import stockProducts
# Create your models here.
    
class pedidos(models.Model):
    nombre = models.TextField()
    DNI = models.IntegerField()
    telefono = models.IntegerField()
    total = models.FloatField()
    estado = models.IntegerField(null = True)  
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
class prodsPedidos(models.Model):
    pedido_id = models.ForeignKey(pedidos, null=True, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(stockProducts,null=True, on_delete=models.CASCADE)
    cantidad = models.IntegerField()