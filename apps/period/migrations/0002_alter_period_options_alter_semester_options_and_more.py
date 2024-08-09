# Generated by Django 5.0.6 on 2024-08-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='period',
            options={'verbose_name': 'Periodo', 'verbose_name_plural': 'Periodos'},
        ),
        migrations.AlterModelOptions(
            name='semester',
            options={'verbose_name': 'Semestre', 'verbose_name_plural': 'Semestres'},
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.IntegerField(verbose_name='Semestre'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester_name',
            field=models.CharField(max_length=20, verbose_name='Nombre Semestre'),
        ),
    ]