# Generated by Django 5.0.4 on 2024-05-03 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario_externo',
            name='responsavel_cpf',
            field=models.DateField(blank=True, max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='usuario_externo',
            name='responsavel_nome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
