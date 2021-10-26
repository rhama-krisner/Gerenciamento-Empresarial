from rest_framework import serializers
from .models import Departamento, Projeto, Funcionarios

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionarios
        fields = '__all__'

class ProjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'horas', 
        'prazo', 'horas_realizadas', 
        'ultimo_calculo_de_horas','departamento']


class DepartamentoSerializer(serializers.ModelSerializer):
    projeto = serializers.SlugRelatedField(many=True, read_only=True, slug_field='nome')
    class Meta:
        model = Departamento
        fields = ['id', 'nome','projeto']
        







