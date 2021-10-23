from django.db import models
from django.db.models.fields.related import ManyToManyField

class Departamento(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    nome = models.CharField(max_length=30, unique=True, blank=False, null=False)
    horas = models.IntegerField(null=False, blank=False)
    prazo = models.DateTimeField(blank=False, null=False)
    horas_realizadas = models.IntegerField(null=False, blank=False)
    ultimo_calculo_de_horas = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    CNH_CHOICE = (
        ('S','Sim'),
        ('N','Não')
    )

    SEXO_CHOICE = (
        ('M','Masculino'),
        ('F', 'Feminino'),
        ('N', 'Não Informar')
    )

    nome = models.CharField(max_length=255, blank=False, null=False, unique=True)
    cpf = models.IntegerField(blank=False, null=False, unique=True)
    rg = models.CharField(max_length=20, blank=False, null=False)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICE, blank=False, null=False)
    data_nascimento = models.DateField(auto_now_add=True, blank=False, null=False)
    cnh = models.CharField(max_length=1, choices=CNH_CHOICE, blank=False, null=False)
    salario = models.FloatField(blank=False, null=False)
    carga_horária = models.IntegerField(null=False, blank=False)

    departamento = ManyToManyField(Departamento)
    projetos = ManyToManyField(Projeto)

    def __str__(self):
        return self.nome


    