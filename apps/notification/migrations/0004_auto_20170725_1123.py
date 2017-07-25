# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_notification_foreignpk'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='action',
            field=models.CharField(choices=[('none', 'none'), ('team_req_join', 'ønsker å bli med i ditt team'), ('team_req_acc', 'har godtatt ditt team forespørsel'), ('team_req_dec', 'har avslått ditt team forespørsel')], default='none', max_length=25),
        ),
    ]
