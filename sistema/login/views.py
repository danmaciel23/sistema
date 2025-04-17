"""""
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # ou para onde quiser
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
"""
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.conf import settings

class login_view(View):

    def get(self, request):
        Contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/veiculos")
        else:
            return render(request, 'login.html', {'mensagem': 'Usuário ou senha inválidos'})
    #obtem os valores nos campos de user e senha no form login.html   
    def post(self, request):
        usuario = request.POST.get('usuario', None)
        senha = request.POST.get('senha', None)

        user = authenticate(request, username = 'usuario', password = 'senha')
        if user is not None:
            #verifica se o usuario nao esta off no sistema
            if user.is_active:
                login(request, user)
                return redirect("/veiculos")
            
            return render( request, 'autenticacao.html',  {'mensagem': 'Usuário inativo'})
        
        return render( request, 'autenticacao.html',  {'mensagem': 'Usuário ou senha inválidos'})
    
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)