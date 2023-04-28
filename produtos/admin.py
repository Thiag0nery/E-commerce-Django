from django.contrib import admin
from . import models

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['prod_nome', 'prod_categoria', 'prod_estoque', 'prod_preco']

admin.site.register(models.ProdutosModels, ProdutoAdmin)
admin.site.register(models.CompraModels)
admin.site.register(models.CategoriaModels)
# Register your models here.
