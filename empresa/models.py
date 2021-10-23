from django.db import models
from django.db.models.fields.related import ManyToManyField

class Departamento(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Funcionarios(models.Model):
    cnhChoice = (
        ('S','Sim'),
        ('N','Não')
    )

    nome = models.CharField(max_length=255, blank=False, null=False, unique=True)
    data_nascimento = models.DateField(auto_now_add=True, blank=False, null=False)
    cnh = models.CharField(max_length=1, choices=cnhChoice, blank=False, null=False)
    salario = models.FloatField(label='R$',max_length=6 ,blank=False, null=False)
    carga_horária = models.IntegerField(max_length=2, null=False, blank=False)