# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wins', '0002_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='likes',
        ),
    ]
