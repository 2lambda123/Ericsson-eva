# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-05 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotator', '0037_auto_20190405_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='channels',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
