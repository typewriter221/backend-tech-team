# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-28 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bellybean', '0005_auto_20180728_1031'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant_name',
            new_name='rest_name',
        ),
    ]