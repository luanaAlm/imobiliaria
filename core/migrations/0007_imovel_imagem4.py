# Generated by Django 3.2.10 on 2021-12-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_depoimento'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='imagem4',
            field=models.ImageField(default=1, upload_to='img_imoveis/%y'),
            preserve_default=False,
        ),
    ]
