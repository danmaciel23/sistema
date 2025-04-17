"""""
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class login(AuthenticationForm):
    class Meta:
        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}),
        }

        #essa parte é para ser usada para fazer o login, enquanto a models pode ser usada tanto para login quanto para cadastro...

        #ESTA FALTANDO A URLS, VIEW E HTML DE LOGIN E AINDA COMPLETAR A MODELS.PY QUE AINDA NAO TEM TODOS OS PARAMETROS PASSADOS NO CLASSE

"""