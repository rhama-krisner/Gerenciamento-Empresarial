# Generated by Django 3.0.8 on 2021-10-28 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0004_auto_20211028_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='departamento',
            name='funcionarios',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='funcionarios',
        ),
        migrations.AddField(
            model_name='projeto',
            name='funcionariosProjeto',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='projeto', to='empresa.Funcionarios'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='projeto',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='departamento', to='empresa.Projeto'),
        ),
    ]