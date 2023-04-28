from django.shortcuts import render,get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from . import models
from . import forms

class Produtos(ListView):
    model = models.ProdutosModels
    template_name = 'produtos/homepage.html'
    context_object_name = 'Produtos'
class Detalhe(DetailView):
    template_name = 'produtos/detalhe.html'
    pk_url_kwarg = 'prod_codigo'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        prod_codigo = self.kwargs.get('prod_codigo')
        self.produto_banco = get_object_or_404(models.ProdutosModels, prod_codigo=prod_codigo)

        self.comprarForms = {
            'compra':forms.Comprar(data=self.request.POST or None),
            'produto':self.produto_banco,
            'produto_banco': forms.Produto(data=self.request.POST or None),
            'usuario': User
        }
        self.comprar = self.comprarForms['compra']
        self.produto = self.comprarForms['produto_banco']
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.comprarForms)
class comprar(Detalhe):


    def post(self,*args,**kwargs):
        usuario = get_object_or_404(User, username=self.request.user.username)
        comprar_quantidade = self.request.POST.get('comp_quantidade')
        comprar_banco = self.comprar.save(commit=False)
        comprar_banco.comp_user = usuario
        comprar_banco.comp_produto = self.produto_banco
        comprar_banco.save()

        estoque = self.produto_banco.prod_estoque
        estoque -= int(comprar_quantidade)

        self.produto_banco.prod_estoque -= int(comprar_quantidade)
        self.produto_banco.save()



        return render(self.request, self.template_name, self.comprarForms)


