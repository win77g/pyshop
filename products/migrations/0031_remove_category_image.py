# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-01-05 10:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_auto_20190105_1258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
    ]