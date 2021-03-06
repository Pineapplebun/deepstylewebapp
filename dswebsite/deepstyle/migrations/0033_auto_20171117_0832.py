# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 08:32
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepstyle', '0032_auto_20171117_0749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='iterations',
            field=models.PositiveIntegerField(default=1000, validators=[django.core.validators.MaxValueValidator(3000, message='Value too high'), django.core.validators.MinValueValidator(500, message='Value too low')], verbose_name='Iterations [500 - 3000] (Higher iterations might output better results, however, at higher processing time)'),
        ),
    ]
