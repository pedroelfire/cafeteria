# Generated by Django 4.2.5 on 2023-09-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nufobot', '0006_mensaje_ai_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensaje',
            name='ai_role',
            field=models.BooleanField(default=True),
        ),
    ]
