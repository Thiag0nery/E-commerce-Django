from django.urls import path
from . import views
app_name = 'produtos'
urlpatterns = [
    path('', views.Produtos.as_view(), name='homepage'),
    path('<prod_codigo>',views.comprar.as_view(), name='detalhe')
]