# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-28 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translate_this', '0002_auto_20170718_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='phrase',
            name='phrase_lang',
            field=models.CharField(default='English', max_length=100),
        ),
        migrations.AlterField(
            model_name='phrase',
            name='translation_lang',
            field=models.CharField(default='Spanish', max_length=100),
        ),
    ]
