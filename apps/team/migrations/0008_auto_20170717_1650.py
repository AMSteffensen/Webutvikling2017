# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-17 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0007_auto_20170717_1540'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teamuser',
            options={'ordering': ('-team_id',)},
        ),
        migrations.AlterField(
            model_name='teamuser',
            name='joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
