# Generated by Django 3.2 on 2022-12-16 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0004_auto_20221212_2135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='marca',
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Producto.marca'),
            preserve_default=False,
        ),
    ]
