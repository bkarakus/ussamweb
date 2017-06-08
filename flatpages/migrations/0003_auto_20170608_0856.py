# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 08:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flatpages', '0002_auto_20170608_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatpage',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='flatpages', to=settings.AUTH_USER_MODEL, verbose_name='Yazarlar'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='flatpages', to='flatpages.FlatPageCategory', verbose_name='Kategoriler'),
        ),
        migrations.AlterField(
            model_name='flatpage',
            name='featured_image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Resim'),
        ),
    ]
