# Generated by Django 4.2.5 on 2023-10-01 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_usuario_istrainer'),
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.usuario'),
        ),
    ]
