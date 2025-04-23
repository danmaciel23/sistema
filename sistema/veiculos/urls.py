from django.urls import path
from .views import ListarVeiculos, CriarVeiculos, EditarVeiculos, ExcluirVeiculos, FotoVeiculo

urlpatterns = [
    path('listar/', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('upload-foto/', FotoVeiculo, name = 'upload-foto'),
    path('editar/<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('criar/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('excluir/<int:pk>/', ExcluirVeiculos.as_view(), name='excluir-veiculos'),
]