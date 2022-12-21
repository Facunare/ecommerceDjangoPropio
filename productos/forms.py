
from django.forms import ModelForm
from productos.models import stockProducts

class stockForm(ModelForm):
    class Meta:
        model = stockProducts
        fields = ['thumbnail', 'nom_prod', 'precio_prod', 'descripcion', 'categoria']
