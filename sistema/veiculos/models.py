from django.db import models
from veiculos.consts import *
from datetime import datetime

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)  
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)  
    foto = models.ImageField(blank=True, null=True, upload_to='veiculo/fotos')
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)  
# Create your models here.
