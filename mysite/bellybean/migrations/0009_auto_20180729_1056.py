# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-07-29 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bellybean', '0008_auto_20180729_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dish_name',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Dish'),
        ),
        migrations.AlterField(
            model_name='order',
            name='restaurant',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='bellybean.Restaurant'),
        ),
    ]
