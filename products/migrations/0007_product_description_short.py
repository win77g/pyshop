# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-11-02 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_price_old'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_short',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
