# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-17 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_night'),
    ]

    operations = [
        migrations.AlterField(
            model_name='night',
            name='astronomical_dawn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='night',
            name='astronomical_dusk',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='night',
            name='civil_dawn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='night',
            name='civil_dusk',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='night',
            name='nautical_dawn',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='night',
            name='nautical_dusk',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
