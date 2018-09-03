# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-02 07:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restraunts', '0002_restrauntinfo_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restrauntinfo',
            name='Slug',
        ),
        migrations.AddField(
            model_name='restrauntinfo',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, unique=True),
            preserve_default=False,
        ),
    ]
