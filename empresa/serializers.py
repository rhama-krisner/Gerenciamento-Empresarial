from rest_framework import fields, serializers
from django.contrib.auth.models import User
from .models import Departamento, Projeto, Funcionarios

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']

class FuncionariosSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Funcionarios
        fields = ['id','nome','cpf','rg','sexo','data_nascimento','cnh','salario','carga_horaria']
        extra_kwarg = {'projeto':{'required':False}}

class ProjetoSerializer(serializers.ModelSerializer):
    funcionarios = FuncionariosSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-id']
        model = Projeto
        fields = ['nome','horas','prazo','horas_realizadas','ultimo_calculo_de_horas','funcionarios']
        extra_kwargs = {'funcionarios':{'required':False}}

class DepartamentoSerializer(serializers.ModelSerializer):
    projeto = ProjetoSerializer(many=True, read_only=True)
    class Meta:
        ordering = ['-id']
        model = Departamento
        fields = ['id','nome', 'projeto']
        extra_kwargs = {'projeto':{'required':False}}



