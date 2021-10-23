from django.contrib import admin
from .models import Departamento,Projeto, Funcionarios

# Register your models here.

class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id','nome')

class FuncionariosAdmin(admin.ModelAdmin):
    list_display = ('id','nome')

admin.site.register(Projeto, ProjetoAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Funcionarios, FuncionariosAdmin)
