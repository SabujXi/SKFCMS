# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='is_reset_req_flag',
            field=models.BooleanField(default=False),
        ),
    ]
