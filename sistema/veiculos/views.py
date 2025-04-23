from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .models import Veiculo
from .forms import VeiculoForm
from django.core.files.storage import FileSystemStorage

class ListarVeiculos(ListView):
    model = Veiculo
    context_object_name = 'veiculos'
    template_name = 'veiculo/listar.html'

class EditarVeiculos(UpdateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo/editar.html'
    success_url = reverse_lazy('listar-veiculos')

class CriarVeiculos(CreateView):
    model = Veiculo
    form_class = VeiculoForm
    template_name = 'veiculo/criar.html'
    success_url = reverse_lazy('listar-veiculos')

class ExcluirVeiculos(DeleteView):
    model = Veiculo
    template_name = 'veiculo/confirmar-exclusao.html'
    success_url = reverse_lazy('listar-veiculos')

def FotoVeiculo(request):
    if request.method == 'POST' and request.FILES['foto']:
        foto = request.FILES['foto']
        fs = FileSystemStorage()
        filename = fs.save(foto.name, foto)
        uploaded_file_url = fs.url(filename)
        return render(request, 'veiculo/foto-upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'veiculo/foto-upload.html')