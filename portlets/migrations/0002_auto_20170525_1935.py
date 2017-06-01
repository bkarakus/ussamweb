# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-25 19:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('portlets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portlet',
            name='content_model',
        ),
        migrations.AddField(
            model_name='portlet',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_portlets.portlet_set+', to='contenttypes.ContentType'),
        ),
    ]