# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mezzanine.core.fields
import mezzanine.pages.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('featured_image', mezzanine.core.fields.FileField(blank=True, max_length=255, verbose_name='Featured Image')),
                ('subtitle', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alt Ba\u015fl\u0131k')),
                ('keywords_string', models.CharField(blank=True, editable=False, max_length=500)),
                ('language', models.CharField(default='', editable=False, max_length=5)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(blank=True, help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL')),
                ('_meta_title', models.CharField(blank=True, help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from')),
                ('expiry_date', models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on')),
                ('short_url', models.URLField(blank=True, null=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('content_model', models.CharField(editable=False, max_length=50, null=True)),
                ('in_menus', mezzanine.pages.fields.MenusField(blank=True, choices=[(1, 'Top navigation bar'), (2, 'Left-hand tree'), (3, 'Footer')], max_length=100, null=True, verbose_name='Show in menus')),
                ('titles', models.CharField(editable=False, max_length=1000, null=True)),
                ('login_required', models.BooleanField(default=False, help_text='If checked, only logged in users can view this page', verbose_name='Login required')),
            ],
            options={
                'ordering': ('titles',),
                'verbose_name': 'Page',
                'verbose_name_plural': 'Pages',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
            bases=('pages.page',),
        ),
        migrations.CreateModel(
            name='RichTextPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Rich text page',
                'verbose_name_plural': 'Rich text pages',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.AddField(
            model_name='page',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='pages.Page'),
        ),
        migrations.AddField(
            model_name='page',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]