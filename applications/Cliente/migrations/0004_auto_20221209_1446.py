# Generated by Django 3.2 on 2022-12-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_auto_20221209_1425'),
        ('Cliente', '0003_auto_20221209_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='changuito',
            field=models.ManyToManyField(to='Producto.Producto', verbose_name='compra del cliente'),
        ),
        migrations.DeleteModel(
            name='Carrito',
        ),
    ]