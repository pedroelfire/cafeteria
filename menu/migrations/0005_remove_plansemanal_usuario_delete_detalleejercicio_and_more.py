# Generated by Django 4.2.5 on 2023-10-02 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_usuario_istrainer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plansemanal',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='DetalleEjercicio',
        ),
        migrations.DeleteModel(
            name='Ejercicio',
        ),
        migrations.DeleteModel(
            name='PlanSemanal',
        ),
    ]