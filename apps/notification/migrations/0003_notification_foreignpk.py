# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0002_auto_20170720_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='foreignPK',
            field=models.PositiveIntegerField(default=10101010),
            preserve_default=False,
        ),
    ]