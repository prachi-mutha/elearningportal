# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2021-03-09 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20160502_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(default='', upload_to=''),
        ),
    ]
