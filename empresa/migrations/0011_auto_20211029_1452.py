# Generated by Django 3.0.8 on 2021-10-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0010_auto_20211029_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionarios',
            name='data_nascimento',
            field=models.DateField(),
        ),
    ]
