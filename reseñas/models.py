from django.db import models
from django.contrib.auth.models import User
from productos.models import stockProducts

# Create your models here.

class valoraciones(models.Model):
    producto = models.ForeignKey(stockProducts, on_delete=models.CASCADE)
    estrellas = models.IntegerField()
    mensaje = models.TextField(max_length=180)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.producto.nom_prod

