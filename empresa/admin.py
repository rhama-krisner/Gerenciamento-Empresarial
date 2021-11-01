from django.contrib import admin
from .models import Departamento,Projeto, Funcionarios

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','cpf','data_nascimento')

admin.site.register(Funcionarios, FuncionarioAdmin)

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome','prazo','horas','horas_realizadas')

admin.site.register(Projeto, ProjetoAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(Departamento, DepartamentoAdmin)


