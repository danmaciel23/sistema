from django.test import TestCase, Client
from django.urls import reverse
from veiculos.models import *
from veiculos.forms import *
from datetime import datetime
from django.contrib.auth.models import User


class TestesModelVeiculo(TestCase):
    def setUp(self):
        self.veiculo = Veiculo.objects.create(
            marca=1,
            modelo='Fusca',
            ano= datetime.now().year,
            cor=2,
            combustivel=3
        )

    def test_is_new(self):
        self.assertTrue(self.veiculo.veiculo_novo)
        self.veiculo.ano = datetime.now().year - 5
        self.assertFalse(self.veiculo.veiculo_novo)

    def test_anos_de_uso(self):
        self.assertEqual(self.veiculo.anos_de_uso(), datetime.now().year - 10)
        self.assertEqual(self.veiculo.anos_de_uso(), 10)

class TestesViewListarVeiculo(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('listar')
        self.veiculo = Veiculo.objects.create(
            marca=1,
            modelo='Fusca',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context.get['veiculos']), 1)

class TestesViewCriarVeiculos(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.url = reverse('criar')
        self.form_data = {
            'marca': 1,
            'modelo': 'Fusca',
            'ano': datetime.now().year,
            'cor': 2,
            'combustivel': 3
        }

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {'marca': 1, 'modelo': 'Fusca', 'ano': datetime.now().year, 'cor': 2, 'combustivel': 3}
        response = self.client.post(self.url, data=data)

        response = self.client.post(self.url, data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar'))

        self.assertEqual(Veiculo.objects.count(), 1)
        self.assertEqual(Veiculo.objects.first().modelo, 'Fusca')

class TestesViewEditarVeiculos(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_login(self.user)
        self.veiculo = Veiculo.objects.create(
            marca=1,
            modelo='Fusca',
            ano=datetime.now().year,
            cor=2,
            combustivel=3
        )
        self.url = reverse('editar', kwargs={'pk'  : self.veiculo.pk})
        self.form_data = {
            'marca': 1,
            'modelo': 'Fusca',
            'ano': datetime.now().year,
            'cor': 2,
            'combustivel': 3
        }

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        data = {'marca': 1, 'modelo': 'Fusca', 'ano': datetime.now().year, 'cor': 2, 'combustivel': 3}
        response = self.client.post(self.url, data=data)

        response = self.client.post(self.url, data=self.form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('listar'))

        veiculo_atualizado = Veiculo.objects.get(id=self.veiculo.id)
        self.assertEqual(veiculo_atualizado.modelo, 'Fusca')
# Create your tests here.

###teste para deletar veiculo TesteViewDeletarVeiculos, 
