# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-07 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopmodel',
            name='locations',
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='city',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='shopmodel',
            name='street',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]