# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 13:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messages', '0006_auto_20170824_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_notif_rel', to='messages.MessageRelation')),
                ('user_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_notif_user_from', to=settings.AUTH_USER_MODEL)),
                ('user_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='msg_notif_user_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('updated',),
            },
        ),
    ]
