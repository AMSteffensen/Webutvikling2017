# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 13:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20170808_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhour',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]