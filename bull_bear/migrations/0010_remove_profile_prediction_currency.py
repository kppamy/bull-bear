# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-23 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bull_bear', '0009_auto_20161123_0347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='prediction_currency',
        ),
    ]