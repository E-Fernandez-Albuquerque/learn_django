# Generated by Django 4.0.4 on 2022-04-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='null', upload_to='img'),
        ),
    ]
