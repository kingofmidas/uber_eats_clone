# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-01 09:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0003_meal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='shor_description',
            new_name='short_description',
        ),
    ]
