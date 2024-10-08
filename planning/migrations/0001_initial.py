# Generated by Django 5.0.4 on 2024-07-08 06:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Exercise', '0004_alter_exercise_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PlannedWorkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('duration', models.DurationField()),
                ('sets', models.IntegerField()),
                ('reps', models.IntegerField()),
                ('rest_interval', models.DurationField()),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exercise.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
