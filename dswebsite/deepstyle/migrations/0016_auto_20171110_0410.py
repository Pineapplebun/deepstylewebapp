# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-10 04:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepstyle', '0015_auto_20171110_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='output_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
