# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-01-05 09:55
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0028_auto_20190105_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=products.models.image_folder),
        ),
    ]