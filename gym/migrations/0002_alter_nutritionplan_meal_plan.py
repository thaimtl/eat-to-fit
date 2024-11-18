# Generated by Django 5.0.7 on 2024-10-31 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutritionplan',
            name='meal_plan',
            field=models.CharField(choices=[('high_carb', 'High carb diet'), ('high_protein', 'High protein diet'), ('high_protein_high_carb_low_fat', 'High protein, high carb, low fat diet')], default='high_carb', max_length=100),
        ),
    ]
