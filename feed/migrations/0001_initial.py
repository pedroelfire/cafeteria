# Generated by Django 4.2.5 on 2023-10-01 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0004_usuario_istrainer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField()),
                ('descripcion', models.TextField()),
                ('fecha_publicacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.usuario')),
            ],
        ),
    ]
