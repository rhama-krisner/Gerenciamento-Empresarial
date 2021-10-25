from rest_framework import serializers
from .models import Departamento, Projeto, Funcionarios

class DepartamentoSerializer(serializers.ModelSerializer):
    projeto = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Departamento
        fields = ['id', 'nome']


class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = ['id', 'nome','cpf','rg','sexo','data_nascimento',
        'cnh','salario','carga_horaria']      


class ProjetoSerializer(serializers.ModelSerializer):
    projeto = serializers.StringRelatedField(many=True)

    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'horas', 
        'prazo', 'horas_realizadas', 
        'ultimo_calculo_de_horas']


