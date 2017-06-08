# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-08 07:36
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_order', mezzanine.core.fields.OrderField(null=True, verbose_name='Order')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('label_tr', models.CharField(max_length=200, null=True, verbose_name='Label')),
                ('label_en', models.CharField(max_length=200, null=True, verbose_name='Label')),
                ('label_ar', models.CharField(max_length=200, null=True, verbose_name='Label')),
                ('field_type', models.IntegerField(choices=[(1, 'Single line text'), (2, 'Multi line text'), (3, 'Email'), (13, 'Number'), (14, 'URL'), (4, 'Check box'), (5, 'Check boxes'), (6, 'Drop down'), (7, 'Multi select'), (8, 'Radio buttons'), (9, 'File upload'), (10, 'Date'), (11, 'Date/time'), (15, 'Date of birth'), (12, 'Hidden')], verbose_name='Type')),
                ('required', models.BooleanField(default=True, verbose_name='Required')),
                ('visible', models.BooleanField(default=True, verbose_name='Visible')),
                ('choices', models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, verbose_name='Choices')),
                ('choices_tr', models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, null=True, verbose_name='Choices')),
                ('choices_en', models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, null=True, verbose_name='Choices')),
                ('choices_ar', models.CharField(blank=True, help_text='Comma separated options where applicable. If an option itself contains commas, surround the option with `backticks`.', max_length=1000, null=True, verbose_name='Choices')),
                ('default', models.CharField(blank=True, max_length=2000, verbose_name='Default value')),
                ('default_tr', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default value')),
                ('default_en', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default value')),
                ('default_ar', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Default value')),
                ('placeholder_text', models.CharField(blank=True, max_length=100, verbose_name='Placeholder Text')),
                ('placeholder_text_tr', models.CharField(blank=True, max_length=100, null=True, verbose_name='Placeholder Text')),
                ('placeholder_text_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Placeholder Text')),
                ('placeholder_text_ar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Placeholder Text')),
                ('help_text', models.CharField(blank=True, max_length=100, verbose_name='Help text')),
                ('help_text_tr', models.CharField(blank=True, max_length=100, null=True, verbose_name='Help text')),
                ('help_text_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Help text')),
                ('help_text_ar', models.CharField(blank=True, max_length=100, null=True, verbose_name='Help text')),
            ],
            options={
                'ordering': ('_order',),
                'abstract': False,
                'verbose_name': 'Field',
                'verbose_name_plural': 'Fields',
            },
        ),
        migrations.CreateModel(
            name='FieldEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_id', models.IntegerField()),
                ('value', models.CharField(max_length=2000, null=True)),
            ],
            options={
                'verbose_name': 'Form field entry',
                'verbose_name_plural': 'Form field entries',
            },
        ),
    ]
