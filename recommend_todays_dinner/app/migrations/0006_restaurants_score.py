# Generated by Django 2.2.7 on 2019-11-30 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_restaurants_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurants',
            name='score',
            field=models.FloatField(default=0),
        ),
    ]
