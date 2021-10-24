from rest_framework import viewsets

from .models import Projeto, Funcionarios, Departamento
from .serializers import ProjetoSerializer, FuncionariosSerializer, DepartamentoSerializer

class Projeto(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class Funcionarios(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer

class Departamento(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
