# Generated by Django 5.1.3 on 2024-11-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0002_ingredient_measurement_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
