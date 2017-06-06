# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='caption_ar',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='slide',
            name='caption_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='slide',
            name='caption_tr',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Caption'),
        ),
        migrations.AddField(
            model_name='slide',
            name='description_ar',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='slide',
            name='description_en',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='slide',
            name='description_tr',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Description'),
        ),
    ]
