from django.test import TestCase
from empresa.models import Departamento, Funcionarios, Projeto

class FuncionariosModelTestCase(TestCase):

    def setUp(self):
        self.funcionario = Funcionarios(
            nome = 'Rhama Krisner',
            cpf = '12241612626',
            rg = 'Mg16653651',
            sexo = 'Masculino',
            data_nascimento = '1994-03-03',
            cnh = 'Não',
            salario = 2500.0,
            carga_horaria = 40
        )

    def test_verifica_atributos_funcionarios(self):
        self.assertEqual(self.funcionario.nome, 'Rhama Krisner')
        self.assertEqual(self.funcionario.cpf, '12241612626')
        self.assertEqual(self.funcionario.rg, 'Mg16653651')
        self.assertEqual(self.funcionario.sexo, 'Masculino')
        self.assertEqual(self.funcionario.data_nascimento, '1994-03-03')
        self.assertEqual(self.funcionario.cnh, 'Não')
        self.assertEqual(self.funcionario.salario, 2500.0)
        self.assertEqual(self.funcionario.carga_horaria, 40)

class ProjetoModelsTestCase(TestCase):

    def setUp(self):
        self.projeto = Projeto(
            nome = 'Cliente',
            horas = 50,
            prazo = '2021-12-21',
            horas_realizadas = 20,
            ultimo_calculo_de_horas = 10
        )
    
    def test_verification_atributos_projeto(self):
        self.assertEqual(self.projeto.nome, 'Cliente')
        self.assertEqual(self.projeto.horas, 50)
        self.assertEqual(self.projeto.prazo, '2021-12-21')
        self.assertEqual(self.projeto.horas_realizadas, 20)
        self.assertEqual(self.projeto.ultimo_calculo_de_horas, 10)


class DepartamentoModelTestCase(TestCase):

    def setUp(self):
        self.departamento = Departamento(
            nome = 'Desenvolvimento'
        )
    
    def test_verifica_atributos_departamento(self):
        self.assertEqual(self.departamento.nome, 'Desenvolvimento')