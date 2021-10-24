from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def empresa(request):
    return Response({'status':200, 'message':'Olá mundo' })
