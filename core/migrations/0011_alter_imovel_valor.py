# Generated by Django 3.2.10 on 2021-12-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_imovel_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imovel',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]
