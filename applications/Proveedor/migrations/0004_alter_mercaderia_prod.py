# Generated by Django 3.2 on 2022-12-12 21:07

import applications.Producto.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proveedor', '0003_auto_20221209_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mercaderia',
            name='prod',
            field=models.CharField(max_length=50, verbose_name=applications.Producto.models.Producto),
        ),
    ]