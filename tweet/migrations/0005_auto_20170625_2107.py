# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0004_auto_20170625_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
