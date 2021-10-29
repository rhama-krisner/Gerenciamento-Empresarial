from django.db import models
from django.db.models import CASCADE

class Funcionarios(models.Model):
    CNH_CHOICE = (
        ('Sim','Sim'),
        ('Não','Não')
    )
    SEXO_CHOICE = (
        ('Masculino','Masculino'),
        ('Feminino', 'Feminino'),
        ('Nenhum', 'Não Informar')
    )

    nome = models.CharField(max_length=255, blank=False, null=False)
    cpf = models.IntegerField(blank=False, null=False, unique=True)
    rg = models.CharField(max_length=20, blank=False, null=False)
    sexo = models.CharField(max_length=9, choices=SEXO_CHOICE, blank=False, null=False)
    data_nascimento = models.DateField(auto_now_add=True, blank=False, null=False)
    cnh = models.CharField(max_length=3, choices=CNH_CHOICE, blank=False, null=False)
    salario = models.FloatField(blank=False, null=False)
    carga_horaria = models.IntegerField(blank=False, null=False)   

    def __str__(self):
        return self.nome  
    
    class Meta:
        ordering = ['id']


class Projeto(models.Model):
    supervisor = models.ManyToManyField('Funcionarios', related_name='supervisor', blank=True)
    nome = models.CharField(max_length=30, unique=True, blank=False, null=False)
    horas = models.IntegerField(null=False, blank=False)
    prazo = models.DateField(blank=False, null=False)
    horas_realizadas = models.IntegerField(null=False, blank=False)
    ultimo_calculo_de_horas = models.IntegerField(blank=False, null=False)

    funcionarios = models.ManyToManyField('Funcionarios', related_name='funcionarios', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['id']  

class Departamento(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    projeto = models.ManyToManyField('Projeto', related_name='projeto', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['id']