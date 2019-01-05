# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2019-01-05 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_productcategory_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=products.models.image_folder),
        ),
    ]