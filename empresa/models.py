from django.db import models
from django.db.models.fields.related import ManyToManyField

class Departamento(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Funcionarios(models.Model):
    
