# Generated by Django 4.1.1 on 2022-12-05 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_delete_compra'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidos',
            name='estado',
            field=models.IntegerField(null=True),
        ),
    ]