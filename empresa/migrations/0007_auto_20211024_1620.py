# Generated by Django 3.0.8 on 2021-10-24 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_auto_20211024_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='cnh',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=3),
        ),
        migrations.AlterField(
            model_name='funcionarios',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino'), ('Nenhum', 'Não Informar')], max_length=9),
        ),
    ]
