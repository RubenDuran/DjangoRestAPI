# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate_this', '0003_auto_20170728_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phrase',
            name='phrase_lang',
            field=models.CharField(default='en-US', max_length=100),
        ),
        migrations.AlterField(
            model_name='phrase',
            name='translation_lang',
            field=models.CharField(default='es-MX', max_length=100),
        ),
    ]
