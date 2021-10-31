import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
import random
from random import randint
from empresa.models import Funcionarios

def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)

    genero = randint(1, 3)
    if genero == 1:
        sexo = 'Masculino'
    elif genero == 2:
        sexo = 'Feminino'
    else:
        sexo = 'Nenhum'
    
    valorcnh = randint(1, 2)
    if valorcnh == 1:
        cnh = 'Sim'
    else:
        cnh = 'Não'
    

    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        cpf = cpf.generate()
        rg = "MG-{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9)) 
        salario = "{}".format(random.randrange(1100.0, 10000.0))
        data_nascimento = "{}-{}-{}".format(random.randrange(1971, 2003), random.randrange(1, 12), random.randrange(1, 29))
        carga_horaria = 40
        p = Funcionarios(nome=nome, cpf=cpf, rg=rg, sexo=sexo, data_nascimento=data_nascimento, cnh=cnh, salario=salario, carga_horaria=carga_horaria )
        p.save()

criando_pessoas(50)
print('Sucesso!')