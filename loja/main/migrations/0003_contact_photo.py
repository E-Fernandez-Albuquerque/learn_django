# Generated by Django 4.0.4 on 2022-04-24 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.ImageField(default='0', upload_to=''),
        ),
    ]
