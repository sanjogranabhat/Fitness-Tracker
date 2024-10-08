# Generated by Django 5.0.6 on 2024-06-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Register', '0002_alter_user_is_admin_alter_user_is_trainer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_trainer',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_user',
        ),
        migrations.AddField(
            model_name='user',
            name='is_customer',
            field=models.BooleanField(default=False, verbose_name='Is customer'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Is employee'),
        ),
    ]
