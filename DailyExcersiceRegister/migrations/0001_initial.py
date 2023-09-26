# Generated by Django 4.2.5 on 2023-09-26 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0003_alter_ejercicio_id_alter_usuario_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroDiario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('observaciones', models.TextField()),
                ('plan_semanal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.detalleejercicio')),
            ],
        ),
    ]