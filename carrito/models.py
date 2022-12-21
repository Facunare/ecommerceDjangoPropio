from django.db import models
from django.contrib.auth.models import User
from productos.models import stockProducts
# Create your models here.


class carrito(models.Model):
    foto = models.ImageField(null=True)
    nom_prod = models.TextField(max_length=200)
    cant_prod = models.IntegerField()
    precio_prod = models.FloatField()
    prod = models.ForeignKey(stockProducts, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.nom_prod
    