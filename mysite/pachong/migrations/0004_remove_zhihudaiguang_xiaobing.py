# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pachong', '0003_zhihudaiguang_xiaobing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zhihudaiguang',
            name='xiaobing',
        ),
    ]