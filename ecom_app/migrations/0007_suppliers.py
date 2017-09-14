# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-11 23:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0006_auto_20170912_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
                ('slug', models.CharField(max_length=120, unique=True)),
                ('description', models.TextField(default='')),
            ],
        ),
    ]
