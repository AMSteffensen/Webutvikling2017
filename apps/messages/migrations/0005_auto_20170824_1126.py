# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-24 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('messages', '0004_auto_20170823_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='msg_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_id', to='messages.MessageRelation'),
        ),
    ]
