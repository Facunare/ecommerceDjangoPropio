# Generated by Django 4.1.1 on 2022-11-05 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0015_compra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='direccion_cliente',
        ),
    ]