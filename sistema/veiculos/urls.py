from django.urls import path
from .views import ListarVeiculos# CriarVeiculos, EditarVeiculos, ExcluirVeiculos, FotoVeiculo

urlpatterns = [
    path('listar/', ListarVeiculos.as_view(), name='listar-veiculos'),
]