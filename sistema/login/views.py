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
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

class login_view(View):

    def get(self, request):
        Contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/veiculos")# #veiculos/listar-veiculos
        else:
            return render(request, 'login.html', Contexto)
    #obtem os valores nos campos de user e senha no form login.html   
    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username = username, password = password)
        if user is not None:
            #verifica se o usuario nao esta off no sistema
            if user.is_active:
                login(request, user)
                return redirect("/veiculos/") #veiculos/listar-veiculos
            
            return render( request, 'login.html',  {'mensagem': 'Usuário inativo'})
        
        return render( request, 'login.html',  {'mensagem': 'Usuário ou senha inválidos'})
    
class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    
    #teria que trocar a url para lista-veiculos para apos o login ele direcionar para a tela de listagem dos carros.../ - / .-. /...

class LoginAPI(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={
                'request': request
            }
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'id': user.id,
            'nome': user.first_name,
            'email': user.email,
            'token': token.key
        })
    
