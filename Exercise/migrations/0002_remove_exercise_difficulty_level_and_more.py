# Generated by Django 5.0.3 on 2024-06-30 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Exercise', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='difficulty_level',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='equipment',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscle_group',
        ),
        migrations.DeleteModel(
            name='DifficultyLevel',
        ),
        migrations.DeleteModel(
            name='Equipment',
        ),
        migrations.DeleteModel(
            name='Exercise',
        ),
        migrations.DeleteModel(
            name='MuscleGroup',
        ),
    ]
