from django.db.models.base import Model
from rest_framework import fields, serializers
from .models import Departamento, Projeto, Funcionarios

class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        fields = ('id', 'nome')

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ('id', 'nome', 'horas', 
        'prazo', 'horas_realizadas', 
        'ultimo_calculo_de_horas')

class FuncionariosSerializer(serializers.ModelSerializer):
    status_code = serializers.IntegerField(source='status.status_code', read_only=True)
    class Meta:
        model = Funcionarios
        fields = ('id', 'nome','cpf','rg','sexo','data_nascimento',
        'cnh','salario','carga_horaria')
