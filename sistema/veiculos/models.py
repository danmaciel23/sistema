from django.db import models
from veiculos.consts import *
from datetime import datetime

class Veiculo(models.Model):
    marca = models.SmallIntegerField(choices=OPCOES_MARCAS)  
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    cor = models.SmallIntegerField(choices=OPCOES_CORES)  
    foto = models.ImageField(blank=True, null=True, upload_to='veiculos/fotos/')
    combustivel = models.SmallIntegerField(choices=OPCOES_COMBUSTIVEIS)  
# Create your models here.
    @property
    def veiculo_novo(self):
        """
        Verifica se o veículo é novo ou usado. retornando True se o veículo for novo (ano atual) e False caso contrário.
        property é util porque nao salva os dados no DB, apenas retorna o valor.
        """
        return self.ano == datetime.now().year
    def anos_de_uso(self):
        """
        Retorna a quantidade de anos que o veículo está em uso.
        """
        return datetime.now().year - self.ano #retorna a diferenaca entre ano dos veiculos gg