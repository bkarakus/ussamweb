# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-26 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slide',
            options={'ordering': ('-publish_date', '_order'), 'verbose_name': 'Resim', 'verbose_name_plural': 'Resimler'},
        ),
        migrations.AddField(
            model_name='slide',
            name='show_on_homepage',
            field=models.BooleanField(default=False, verbose_name='Anasayfada g\xf6ster'),
        ),
    ]