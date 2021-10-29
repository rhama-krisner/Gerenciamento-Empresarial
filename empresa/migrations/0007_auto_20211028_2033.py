# Generated by Django 3.0.8 on 2021-10-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0006_auto_20211028_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='nome',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='funcionarios',
            field=models.ManyToManyField(blank=True, related_name='funcionarios', to='empresa.Funcionarios'),
        ),
    ]
