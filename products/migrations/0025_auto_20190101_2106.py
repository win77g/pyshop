# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-01-01 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20181228_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productimage',
            options={},
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=products.models.image_folder),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default=None, null=True),
        ),
    ]
