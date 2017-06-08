# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields
import mezzanine.utils.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_tr', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('_meta_title_tr', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('_meta_title_en', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('_meta_title_ar', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('description_tr', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('description_ar', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('content_tr', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_en', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_ar', mezzanine.core.fields.RichTextField(null=True, verbose_name='Content')),
                ('featured_image', mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Featured Image')),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': 'D\xfcz Sayfa',
                'verbose_name_plural': 'D\xfcz Sayfalar',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='FlatPageCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('title_tr', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_en', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('title_ar', models.CharField(max_length=500, null=True, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Kategori',
                'verbose_name_plural': 'Kategoriler',
            },
        ),
    ]
