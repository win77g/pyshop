# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-12-28 12:16
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0023_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description_short',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
