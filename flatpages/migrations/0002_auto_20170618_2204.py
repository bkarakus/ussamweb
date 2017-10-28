# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 22:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('flatpages', '0001_initial'),
        ('pages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatPageIndex',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.Page')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flatpages.FlatPageCategory')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Kategori Index',
                'verbose_name_plural': 'Kategori Index Sayfalar\u0131',
            },
            bases=('pages.page',),
        ),
        migrations.AddField(
            model_name='flatpagecategory',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='authors',
            field=models.ManyToManyField(blank=True, related_name='flatpages', to=settings.AUTH_USER_MODEL, verbose_name='Yazarlar'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='flatpages', to='flatpages.FlatPageCategory', verbose_name='Kategoriler'),
        ),
        migrations.AddField(
            model_name='flatpage',
            name='site',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
        ),
    ]
