# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploademail',
            name='upload',
            field=models.FileField(blank=True, null=True, upload_to=b'/uploads/'),
        ),
    ]
