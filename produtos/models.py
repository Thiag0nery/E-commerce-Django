from django.db import models
from django.contrib.auth.models import User
class CategoriaModels(models.Model):
    cate_codigo = models.BigAutoField(primary_key=True)
    cate_nome = models.CharField(max_length=80)

    def __str__(self):
        return self.cate_nome
class ProdutosModels(models.Model):
    prod_codigo = models.BigAutoField(primary_key=True)
    prod_nome = models.CharField(max_length=80, verbose_name='Nome')
    prod_categoria = models.ForeignKey(CategoriaModels, on_delete=models.CASCADE, verbose_name='Categoria')
    prod_estoque = models.IntegerField(max_length=200, verbose_name='Estoque')
    prod_preco = models.FloatField(max_length=20, verbose_name='Preço')
    def __str__(self):
        return self.prod_nome
class CompraModels(models.Model):
    comp_codigo = models.BigAutoField(primary_key=True)
    comp_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    comp_produto = models.ForeignKey(ProdutosModels, on_delete=models.CASCADE, null=True,blank=True)
    comp_quantidade = models.IntegerField(null=True,blank=True)