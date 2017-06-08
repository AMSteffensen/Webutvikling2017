# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobName', models.CharField(max_length=250)),
                ('jobDescription', models.TextField(max_length=10000)),
                ('jobTaken', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Principal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('county', models.CharField(max_length=100)),
                ('zipcode', models.IntegerField()),
                ('street', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('verified', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='jobAuthor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Principal'),
        ),
    ]
