# Generated by Django 2.2.7 on 2019-11-29 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=20)),
                ('contents', models.CharField(max_length=500)),
                ('score', models.IntegerField(default=0)),
                ('restaurant', models.ForeignKey(on_delete='CASCADE', to='app.Restaurant')),
            ],
        ),
    ]
