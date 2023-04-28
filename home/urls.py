from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('cadastro/', views.Cadastro.as_view(), name='cadastro')
]