# Generated by Django 4.2.5 on 2023-09-28 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nufobot', '0003_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='respuesta',
            field=models.TextField(default=0),
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]