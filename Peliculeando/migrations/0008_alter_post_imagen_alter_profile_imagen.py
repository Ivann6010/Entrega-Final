# Generated by Django 4.1.7 on 2023-04-21 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Peliculeando', '0007_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(upload_to='img'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='imagen',
            field=models.ImageField(upload_to='img-pro'),
        ),
    ]