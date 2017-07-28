# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0004_auto_20170725_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='action',
            field=models.CharField(choices=[('none', 'none'), ('team_req_join', 'ønsker å bli med i ditt team'), ('team_req_acc', 'har godtatt ditt team forespørsel'), ('team_req_dec', 'har avslått ditt team forespørsel'), ('team_invite', 'har invitert deg til team'), ('team_invite_acc', 'har godtatt din team invitasjon'), ('team_invite_dec', 'har avslått din team invitasjon')], default='none', max_length=25),
        ),
    ]