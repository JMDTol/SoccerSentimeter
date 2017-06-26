# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0006_auto_20170626_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
