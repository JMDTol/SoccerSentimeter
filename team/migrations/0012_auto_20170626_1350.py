# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_auto_20170626_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='volume',
            field=models.IntegerField(default=25),
        ),
    ]
