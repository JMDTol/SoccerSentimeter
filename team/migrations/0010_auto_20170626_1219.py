# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 16:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_auto_20170626_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='firstName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
