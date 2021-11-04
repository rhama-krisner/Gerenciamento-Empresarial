from rest_framework.test import APITestCase
from empresa.models import Funcionarios
from django.urls import reverse
from rest_framework import status

class FuncionariosTestCase(APITestCase):

    def setUp(self):
        self.list_funcionarios_url = reverse('funcionarios')
        self.funcionario_1 = Funcionarios.objects.create(
            nome = 'Teste1', 
            cpf = '38395053053', 
            rg = 'MG-12345678', 
            sexo = 'Masculino', 
            data_nascimento = '1994-12-12', 
            cnh = 'Sim', 
            salario = 1100, 
            carga_horaria = 40,
        )
    
    def test_GET(self):
        """Teste para verificar a requisição GET"""
        
        response = self.client.get(self.list_funcionarios_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_POST(self):
        """Teste para verificar a requisição POST para adicionar um novo funcionário"""
        data = {
            "nome": "Teste",
            "cpf": "83540491082",
            "rg": "MG-16653651",
            "sexo": "Masculino",
            "data_nascimento": "03-03-1994",
            "cnh": "Sim",
            "salario": 3500.0,
            "carga_horaria": 40
        }

        response = self.client.post(self.list_funcionarios_url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_DELETE(self):
        """Teste para verificar a requisição DELETE"""

        response = self.client.delete('/funcionarios/1/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_PUT(self):
        """Teste para verificar a requisição PUT"""

        data = {
            "id":1,
            "nome": "Luiz Henrique Rodrigues",
            "cpf": "35763877225",
            "rg": "MG-451377240",
            "sexo": "Masculino",
            "data_nascimento": "28-07-1990",
            "cnh": "Não",
            "salario": 4401.0,
            "carga_horaria": 40
        }
        response = self.client.put('/funcionarios/1', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

