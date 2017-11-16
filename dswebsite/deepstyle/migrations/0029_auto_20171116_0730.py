# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 07:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepstyle', '0028_auto_20171115_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='style_blend_weight',
            field=models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(1.0, message='Value too high'), django.core.validators.MinValueValidator(0.0, message='Value too low')], verbose_name='Style Blend Weight [0.0 - 1.0]'),
        ),
        migrations.AlterField(
            model_name='job',
            name='content_weight',
            field=models.FloatField(default=5.0, verbose_name='Content Weight [Any value relative to style weight]'),
        ),
        migrations.AlterField(
            model_name='job',
            name='content_weight_blend',
            field=models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(1.0, message='Value too high'), django.core.validators.MinValueValidator(0.0, message='Value too low')], verbose_name='Content Weight Blend [0.0 - 1.0]'),
        ),
        migrations.AlterField(
            model_name='job',
            name='learning_rate',
            field=models.FloatField(default=10.0, verbose_name='Learning Rate [~10] (Best kept at default)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='style_layer_weight_exp',
            field=models.FloatField(default=1, verbose_name='Style Layer Weight Exp [Any value] (Lower value results in more detailed output)'),
        ),
        migrations.AlterField(
            model_name='job',
            name='style_scale',
            field=models.FloatField(default=1.0, verbose_name='Style Scale [~0.5 - ~2.0]'),
        ),
        migrations.AlterField(
            model_name='job',
            name='style_weight',
            field=models.FloatField(default=500.0, verbose_name='Style Weight [Any value relative to content weight]'),
        ),
    ]
