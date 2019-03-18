# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-18 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('wins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pyuploadcare.dj.models.ImageField(blank=True)),
                ('name', models.CharField(blank=True, max_length=31)),
                ('caption', models.CharField(blank=True, max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to='wins.User')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wins.User')),
            ],
        ),
    ]