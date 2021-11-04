from rest_framework.test import APITestCase
from empresa.models import Projeto, Funcionarios
from django.urls import reverse
from rest_framework import status

class ProjetoTestCase(APITestCase):
    def setUp(self):
        
        self.list_projeto_url = reverse('projeto')
        self.projeto_1 = Projeto.objects.create(
            supervisor = [],
            nome = 'Teste',
            horas = 30,
            prazo = '2021-11-05',
            horas_realizadas = 25,
            ultimo_calculo_de_horas = 30,
            funcionario = []
        )
    
    def test_GET(self):        
        """Teste para verificar a requisição GET"""
        response = self.client.get(self.list_projeto_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
