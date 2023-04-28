from django import forms
from . import models
class Comprar(forms.ModelForm):
    class Meta:
        model = models.CompraModels
        fields = '__all__'
class Produto(forms.ModelForm):
    class Meta:
        model = models.ProdutosModels
        fields = '__all__'