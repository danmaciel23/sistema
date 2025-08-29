from winreg import DeleteKey
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, View, DeleteView
from .models import Veiculo
from .forms import FormularioVeiculo
##from django.core.files.storage import object
from django.http import FileResponse, HttpResponseNotFound, Http404
from rest_framework.generics import ListAPIView, DestroyAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from veiculos.serializers import SerealizadorVeiculo
from sistema import settings
import os


class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class EditarVeiculos(UpdateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class ExcluirVeiculos(DeleteView):
    model = Veiculo
    template_name = 'veiculo/excluir.html'
    success_url = reverse_lazy('listar-veiculos')

class CriarVeiculos(CreateView):
    model = Veiculo
    form_class = FormularioVeiculo
    template_name = 'veiculo/novo.html'
    success_url = reverse_lazy('listar-veiculos')

class FotoVeiculo(View):

    def get(self, request, arquivo):
        try:
            veiculo = Veiculo.objects.get(foto='veiculos/fotos/{}' .format(arquivo))

            caminho_arquivo = os.path.join(settings.MEDIA_ROOT, veiculo.foto.name)

        # Verifica se o arquivo realmente existe
            if not os.path.exists(caminho_arquivo):
                raise Http404("Arquivo não encontrado")

            # Retorna o arquivo como resposta
            return FileResponse(open(caminho_arquivo, 'rb'), content_type='image/jpeg')

        except Veiculo.DoesNotExist:
            raise Http404("Veículo com essa foto não encontrado")
        except Exception as e:
            raise Http404(f"Erro ao acessar o arquivo: {str(e)}")
            
class APIListaVeiculos(ListAPIView):
    """
    API para listar veículos.
    """
    serializer_class = SerealizadorVeiculo 
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Retorna todos os veículos.
        """
        return Veiculo.objects.all()
    

class APIDeletarVeiculo(DestroyAPIView):
    """
    API para excluir um veículo.
    """
    queryset = Veiculo.objects.all()
    serializer_class = SerealizadorVeiculo
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Retorna o veículo a ser excluído.
        """
        return Veiculo.objects.all()