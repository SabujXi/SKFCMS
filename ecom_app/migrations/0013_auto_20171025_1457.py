# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-25 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom_app', '0012_auto_20171025_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock_status',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
