# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-01-01 22:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_remove_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
