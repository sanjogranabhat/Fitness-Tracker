# Generated by Django 5.0.6 on 2024-06-24 09:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DifficultyLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MuscleGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('thumbnail', models.ImageField(upload_to='thumbnails/')),
                ('instructions', models.TextField()),
                ('video_url', models.URLField(blank=True)),
                ('difficulty_level', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Exercise.difficultylevel')),
                ('equipment', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Exercise.equipment')),
                ('muscle_group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Exercise.musclegroup')),
            ],
        ),
    ]
