# Generated by Django 3.2.10 on 2021-12-21 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_imovel_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imovel',
            old_name='Tipo',
            new_name='tipo',
        ),
    ]
