# Generated by Django 2.0.9 on 2019-01-06 16:33

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='name',
            field=models.CharField(max_length=250, verbose_name=django.contrib.auth.models.User),
        ),
    ]
