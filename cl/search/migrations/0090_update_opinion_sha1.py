# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2020-01-08 18:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0089_add_more_courts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='sha1',
            field=models.CharField(blank=True, db_index=True, help_text=b'unique ID for the document, as generated via SHA1 of the binary file or text data', max_length=40),
        ),
    ]