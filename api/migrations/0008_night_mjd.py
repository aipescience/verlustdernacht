# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-28 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_moonposition'),
    ]

    operations = [
        migrations.AddField(
            model_name='night',
            name='mjd',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
