# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 00:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0007_auto_20170405_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diplome',
            old_name='nbr_redublements',
            new_name='nbr_redoublements',
        ),
    ]
