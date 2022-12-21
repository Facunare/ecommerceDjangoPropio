from django.db import models
from categoria.models import categorias

# Create your models here.


class stockProducts(models.Model):
    thumbnail = models.ImageField(null=True, upload_to='products')
    nom_prod = models.CharField(max_length=50)   
    precio_prod = models.FloatField()   
    descripcion = models.TextField(max_length=250)
    categoria = models.ForeignKey(categorias, on_delete=models.CASCADE)
    hayStock = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nom_prod