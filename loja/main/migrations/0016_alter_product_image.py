# Generated by Django 4.0.4 on 2022-04-26 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='images'),
        ),
    ]