from rest_framework import serializers
from .models import Departamento, Projeto, Funcionarios

class ProjetoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projeto
        fields = ['id', 'nome', 'horas', 
        'prazo', 'horas_realizadas', 
        'ultimo_calculo_de_horas','departamento']

class DepartamentoSerializer(serializers.ModelSerializer):
    projeto = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Departamento
        fields = ['id', 'nome','projeto']
        


class FuncionariosSerializer(serializers.ModelSerializer):   

    class Meta:
        model = Funcionarios
        fields = '__all__'




