# Generated by Django 3.0.8 on 2021-11-04 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=20)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Nenhum', 'Não Informar')], max_length=9)),
                ('data_nascimento', models.DateField()),
                ('cnh', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3)),
                ('salario', models.FloatField()),
                ('carga_horaria', models.IntegerField(default=40)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, unique=True)),
                ('horas', models.IntegerField()),
                ('prazo', models.DateField()),
                ('horas_realizadas', models.IntegerField()),
                ('ultimo_calculo_de_horas', models.IntegerField()),
                ('funcionarios', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='funcionarios', to='empresa.Funcionarios')),
                ('supervisor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='supervisor', to='empresa.Funcionarios')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, unique=True)),
                ('projeto', models.ManyToManyField(blank=True, related_name='projeto', to='empresa.Projeto')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
