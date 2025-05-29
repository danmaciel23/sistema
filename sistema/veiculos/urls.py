from django.urls import path
from .views import *

urlpatterns = [
    path('', ListarVeiculos.as_view(), name='listar-veiculos'),
    path('fotos/<str:arquivo>/', FotoVeiculo.as_view(), name = 'fotos'),
    path('editar/<int:pk>/', EditarVeiculos.as_view(), name='editar-veiculos'),
    path('novo/', CriarVeiculos.as_view(), name='criar-veiculos'),
    path('api/', APIListaVeiculos.as_view(), name='api-listar-veiculos'),
]