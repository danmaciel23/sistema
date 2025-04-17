"""""
from django.db import models
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    nome_completo = models.CharField(max_length=255, blank= True, null=True)
    is_active = bool
    is_superuser = bool
    password = hash

    #mais ou menos como seria o model da classe usuario(usando user padrao do python)
    #falta ainda algumas coisa, acredito que falte o construtor dessa classe...
    #isso eu tive na resposta do gemini na conta da uft... testar depois com chat gpt...
"""
# Create your models here.
