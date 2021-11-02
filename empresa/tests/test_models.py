from django.test import TestCase
from empresa.models import Funcionarios

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


