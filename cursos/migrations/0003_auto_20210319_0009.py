# Generated by Django 2.2.9 on 2021-03-19 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20210319_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='avaliacao',
            field=models.DecimalField(decimal_places=1, max_digits=2),
        ),
    ]
