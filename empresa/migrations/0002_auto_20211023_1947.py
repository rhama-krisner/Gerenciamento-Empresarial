# Generated by Django 3.0.8 on 2021-10-23 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='prazo',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='ultimo_calculo_de_horas',
            field=models.TimeField(),
        ),
    ]