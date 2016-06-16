# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 19:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('omniforms', '0011_auto_20160614_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='omnidecimalfield',
            name='decimal_places',
            field=models.PositiveIntegerField(default=99999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='omnidecimalfield',
            name='max_digits',
            field=models.PositiveIntegerField(default=9999999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='omnidecimalfield',
            name='max_value',
            field=models.DecimalField(blank=True, decimal_places=999, max_digits=1000, null=True),
        ),
        migrations.AddField(
            model_name='omnidecimalfield',
            name='min_value',
            field=models.DecimalField(blank=True, decimal_places=999, max_digits=1000, null=True),
        ),
    ]
