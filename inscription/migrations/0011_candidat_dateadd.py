# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0010_auto_20170408_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidat',
            name='dateAdd',
            field=models.DateField(blank=True, null=True, verbose_name="Date d'ajout"),
        ),
    ]