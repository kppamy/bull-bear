# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 02:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bull_bear', '0004_event_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='outcome',
            old_name='choice_text',
            new_name='name',
        ),
        migrations.AddField(
            model_name='outcome',
            name='description',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]