# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-02 20:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fcm_django', '0002_auto_20160808_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.TextField(max_length=20, null=True)),
                ('pos_latitude', models.FloatField(null=True)),
                ('pos_longitude', models.FloatField(null=True)),
                ('pos_timestamp', models.DateTimeField(null=True)),
                ('device', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fcm_django.FCMDevice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=250, null=True)),
                ('linked', models.ManyToManyField(to='agents.Group')),
                ('members', models.ManyToManyField(to='agents.Agent')),
            ],
            options={
                'permissions': (('read_members', 'Can read group members data'), ('change_members', 'Can edit group members')),
            },
        ),
    ]
