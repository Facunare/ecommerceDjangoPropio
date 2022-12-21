from django.db import models

# Create your models here.
class categorias(models.Model):
    nombre_cat = models.CharField(max_length=50)
    activo = models.BooleanField(default=True)
    def __str__(self) -> str:
            return self.nombre_cat
