from .models import Projeto, Departamento, Funcionarios
from .serializers import ProjetoSerializer, DepartamentoSerializer, FuncionariosSerializer

from rest_framework import viewsets

class ProjetoView(viewsets.ModelViewSet):
    queryset = Projeto.objects.all()
    serializer_class = ProjetoSerializer

class DepartamentoView(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer


class Funcionarios(viewsets.ModelViewSet):
    queryset = Funcionarios.objects.all()
    serializer_class = FuncionariosSerializer