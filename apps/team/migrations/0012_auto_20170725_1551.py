# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0011_teamjoin_invited'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamjoin',
            name='team_id',
        ),
        migrations.RemoveField(
            model_name='teamjoin',
            name='user_ask',
        ),
        migrations.DeleteModel(
            name='TeamJoin',
        ),
    ]
