# Generated by Django 4.1.1 on 2022-10-28 23:56

from django.db import migrations, models
import ecommerce.models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockproducts',
            name='image_prod',
            field=models.ImageField(blank=True, null=True, upload_to=ecommerce.models.marketplace_directory_path),
        ),
    ]