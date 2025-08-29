from rest_framework import serializers
from .models import Veiculo
##aqui temos a serialização do modelo Veiculo, que é usado para converter os dados do modelo em um formato JSON ou XML, que pode ser facilmente consumido por APIs ou outras aplicações.

class SerealizadorVeiculo(serializers.ModelSerializer):
    
    nome_marca = serializers.SerializerMethodField()
    nome_cor = serializers.SerializerMethodField()
    nome_combustivel = serializers.SerializerMethodField()
    
    class Meta:
        model = Veiculo
        exclude = []

    
    def get_nome_marca(self, instancia):
        return instancia.get_marca_display()
    
    def get_nome_cor(self, instancia):
        return instancia.get_cor_display()
    
    def get_nome_combustivel(self, instancia):
        return instancia.get_combustivel_display()
        