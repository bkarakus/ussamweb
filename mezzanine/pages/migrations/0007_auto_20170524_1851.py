# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-24 18:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20170524_1832'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='image',
            new_name='featured_image',
        ),
    ]
