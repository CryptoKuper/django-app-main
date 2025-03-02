# Generated by Django 5.1.3 on 2024-12-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipeapp', '0007_recipe_ingredients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name', 'measurement_unit']},
        ),
        migrations.AddField(
            model_name='recipe',
            name='dish_image',
            field=models.FileField(null=True, upload_to='recipes/images/'),
        ),
    ]
