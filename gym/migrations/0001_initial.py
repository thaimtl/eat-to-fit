# Generated by Django 5.0.7 on 2024-10-31 20:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NutritionPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_plan', models.CharField(choices=[('high_carb', 'High carb diet'), ('high_protein', 'High protein diet'), ('high_protein_high_carb_low_fat', 'High protein, high carb, low fat diet')], default='high_carb', max_length=50)),
                ('calories', models.FloatField(blank=True, null=True)),
                ('bmi', models.FloatField(blank=True, null=True)),
                ('protein', models.FloatField(blank=True, null=True)),
                ('carbs', models.FloatField(blank=True, null=True)),
                ('fats', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('fitness_goal', models.CharField(choices=[('light', 'Light'), ('moderate', 'Moderate'), ('intense', 'Intense')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_exercise', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]