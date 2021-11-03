from django.test import TestCase
from empresa.models import Funcionarios
from empresa.serializers import FuncionariosSerializer

class FuncionariosSerializerTestCase(TestCase):

    def setUp(self):
        self.funcionarios = Funcionarios(
            nome = 'Rhama Krisner',
            cpf = '12241612626',
            rg = 'Mg16653651',
            sexo = 'Masculino',
            data_nascimento = '1994-03-03',
            cnh = 'Não',
            salario = 2500.0,
            carga_horaria = 40
        )
        self.serializer = FuncionariosSerializer(instance=self.funcionarios)

    def test_verifica_campos_serializados(self):

        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['id','nome','cpf','rg','sexo','data_nascimento','cnh','salario','carga_horaria']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        
        data = self.serializer.data
        self.assertEqual(data['nome'], self.funcionarios.nome)
        self.assertEqual(data['cpf'], self.funcionarios.cpf)
        self.assertEqual(data['rg'], self.funcionarios.rg)
        self.assertEqual(data['sexo'], self.funcionarios.sexo)
        self.assertEqual(data['data_nascimento'], self.funcionarios.data_nascimento)
        self.assertEqual(data['cnh'], self.funcionarios.cnh)
        self.assertEqual(data['salario'], self.funcionarios
        .salario)
        self.assertEqual(data['carga_horaria'], self.funcionarios.carga_horaria)