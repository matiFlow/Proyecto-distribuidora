# Generated by Django 3.2 on 2022-12-26 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0009_delete_marca'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50, verbose_name='marca del producto')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Producto.marca'),
        ),
    ]
