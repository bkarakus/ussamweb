# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-28 17:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('portlets', '0002_auto_20171028_1656'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideShowPortlet',
            fields=[
                ('portlet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portlets.Portlet')),
                ('template', models.CharField(blank=True, choices=[(b'portlets/slideshow.html', '\xd6n Tan\u0131ml\u0131')], default=b'portlets/slideshow.html', max_length=100, null=True, verbose_name='Tema Dosyas\u0131')),
                ('count', models.PositiveSmallIntegerField(default=10, help_text='G\xf6sterilecek slide say\u0131s\u0131', verbose_name='Say\u0131')),
                ('width', models.PositiveSmallIntegerField(default=0, verbose_name='Resim Geni\u015fli\u011fi')),
                ('height', models.PositiveSmallIntegerField(default=0, verbose_name='Resim Y\xfcksekli\u011fi')),
            ],
            options={
                'verbose_name': 'Slideshow Mod\xfcl\xfc',
                'verbose_name_plural': 'Slideshow Mod\xfclleri',
            },
            bases=('portlets.portlet',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
