# Generated by Django 5.0.4 on 2024-07-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
