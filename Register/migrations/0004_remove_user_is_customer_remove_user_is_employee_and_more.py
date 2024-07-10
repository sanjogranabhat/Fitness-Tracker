# Generated by Django 5.0.6 on 2024-06-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0003_remove_user_is_trainer_remove_user_is_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_customer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_employee',
        ),
        migrations.AddField(
            model_name='user',
            name='is_trainer',
            field=models.BooleanField(default=False, verbose_name='Is trainer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_user',
            field=models.BooleanField(default=False, verbose_name='Is user'),
        ),
    ]
