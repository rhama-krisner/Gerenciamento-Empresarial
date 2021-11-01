from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Departamento, Projeto, Funcionarios
from .serializers import DepartamentoSerializer, ProjetoSerializer, FuncionariosSerializer
from rest_framework.pagination import PageNumberPagination
import django_filters

#Funcionarios
@api_view(['GET','POST'])
def funcionario_list(request):
    if request.method =='GET':
        funcionario = Funcionarios.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(funcionario, request)
        serializer = FuncionariosSerializer(page,many=True)
        return paginator.get_paginated_response(serializer.data)
        
    elif request.method == 'POST':
        serializer = FuncionariosSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def funcionario_detail(request, pk):
    try:
        funcionario = Funcionarios.objects.get(pk=pk)
    except Funcionarios.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuncionariosSerializer(funcionario)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = FuncionariosSerializer(funcionario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        funcionario.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Projeto
@api_view(['GET','POST'])
def projeto_list(request):
    if request.method == 'GET':
        projeto = Projeto.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(projeto, request)
        serializer = ProjetoSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProjetoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def projeto_detail(request, pk):
    try:
        projeto = Projeto.objects.get(pk=pk)
    except Projeto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjetoSerializer(projeto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjetoSerializer(projeto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        projeto.delete()
        return Response(status.HTTP_204_NO_CONTENT)

#Departamento
@api_view(['GET','POST'])
def departamento_list(request):
    if request.method == 'GET':
        departamento = Departamento.objects.all()
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(departamento, request)
        serializer = DepartamentoSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def departamento_detail(request, pk):
    try:
        departamento = Departamento.objects.get(pk=pk)
    except Departamento.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DepartamentoSerializer(departamento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    
    elif request.method == 'DELETE':
        departamento.delete()
