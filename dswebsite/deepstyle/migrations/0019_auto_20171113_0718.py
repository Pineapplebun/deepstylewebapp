# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 07:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deepstyle', '0018_auto_20171110_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='output_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
