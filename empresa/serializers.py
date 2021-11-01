from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Departamento, Projeto, Funcionarios
from .validators import *

class FuncionariosSerializer(serializers.ModelSerializer):
    data_nascimento = serializers.DateField(input_formats=['%d-%m-%Y'])
    class Meta:
        ordering = ['-id']
        model = Funcionarios
        fields = ['id','nome','cpf','rg','sexo','data_nascimento','cnh','salario','carga_horaria']
        extra_kwarg = {'projeto':{'required':False}}

    def validate(self, data):
        if nomeValido(data['nome']):
            raise serializers.ValidationError({'nome':'Não inclua números neste campo.'})

        if not cpfValido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido.'})  

        if salario_valido(data['salario']):
            raise serializers.ValidationError({'salario':'Valor e salario inválido. Abaixo de um salário mínimo.'})

        return data

class ProjetoSerializer(serializers.ModelSerializer):
    funcionarios = FuncionariosSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-id']
        model = Projeto
        fields = ['id','nome','supervisor','horas','prazo','horas_realizadas','ultimo_calculo_de_horas','funcionarios']
        extra_kwargs = {'funcionarios':{'required':False}}

    def validate(self, data):
        if data['horas'] > 40:
            raise serializers.ValidationError({'supervisor':'Quantidade de horas acima da carga horaria do supervisor'})
        return data
        
class DepartamentoSerializer(serializers.ModelSerializer):
    projeto = ProjetoSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-id']
        model = Departamento
        fields = ['id','nome', 'projeto']
        extra_kwargs = {'projeto':{'required':False}}



 