# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-12 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sites', models.ManyToManyField(blank=True, to='sites.Site', verbose_name='Sites')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sitepermissions', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name': 'Site permission',
                'verbose_name_plural': 'Site permissions',
            },
        ),
    ]
