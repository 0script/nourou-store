# Generated by Django 4.0.3 on 2022-03-23 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_products_image_main'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sexe',
        ),
        migrations.AddField(
            model_name='category',
            name='brand',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]