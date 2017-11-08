# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-07 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deepstyle', '0008_auto_20171107_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='input_image_path',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='deepstyle.Image'),
        ),
        migrations.AlterField(
            model_name='job',
            name='style_image_path',
            field=models.ForeignKey(null='False', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='deepstyle.Image'),
        ),
    ]