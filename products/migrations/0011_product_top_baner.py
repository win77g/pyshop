# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-11-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20181103_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='top_baner',
            field=models.BooleanField(default=False),
        ),
    ]
