# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-14 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='visits',
            field=models.IntegerField(default=0),
        ),
    ]
