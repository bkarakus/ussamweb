# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-10-28 16:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0002_auto_20170618_2204'),
        ('portlets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryPortlet',
            fields=[
                ('portlet_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='portlets.Portlet')),
                ('count', models.PositiveSmallIntegerField(default=10, help_text='G\xf6sterilecek sayfa say\u0131s\u0131', verbose_name='Say\u0131')),
                ('width', models.PositiveSmallIntegerField(default=0, verbose_name='Resim Geni\u015fli\u011fi')),
                ('height', models.PositiveSmallIntegerField(default=0, verbose_name='Resim Y\xfcksekli\u011fi')),
                ('template', models.CharField(blank=True, choices=[(b'portlets/category.html', '\xd6n Tan\u0131ml\u0131'), (b'portlets/category_news.html', 'Haberler'), (b'portlets/category_vertical.html', 'Yukar\u0131 Do\u011fru Kayan')], default=b'portlets/category.html', max_length=100, null=True, verbose_name='Tema Dosyas\u0131')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flatpages.FlatPageCategory')),
            ],
            options={
                'verbose_name': 'Kategori Mod\xfcl\xfc',
                'verbose_name_plural': 'Kategori Mod\xfclleri',
            },
            bases=('portlets.portlet',),
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='textportlet',
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('base_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]