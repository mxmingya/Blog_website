# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-06 01:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 6, 1, 31, 1, 929836, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
