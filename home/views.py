from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import login,authenticate
from . import forms

class Home(View):
    template_name = 'home/index.html'
    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        self.formulario = {
            'user': forms.UserForm(
                data=self.request.POST or None,

            )
        }
        self.usuarioFormulario = self.formulario['user']
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.formulario)
class Login(Home):
    def post(self, *args, **kwargs):
        usuario = self.request.POST.get('username')
        senha = self.request.POST.get('password')

        if not usuario or not senha:
            print('Erro 1')
            return redirect('home:login')
        usuario = authenticate(
            self.request, username=usuario, password=senha)

        if not usuario:
            print('Erro 2')
            return redirect('home:login')

        login(self.request, user=usuario)
        print('certo')
        return redirect('produtos:homepage')
class Cadastro(Home):
    template_name = 'home/cadastro.html'
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name, self.formulario)
    def post(self, *args, **kwargs):
        if not self.usuarioFormulario.is_valid():
            return render(self.request, self.template_name, self.formulario)
        senha = self.request.POST.get('password')
        username = self.usuarioFormulario.save(commit=False)
        username.set_password(senha)
        username.save()
        template_name = 'home/index.html'
        return render(self.request, template_name, self.formulario)

