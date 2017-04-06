# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inscription', '0006_auto_20170404_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='diplome',
            name='nbr_redublements',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True, verbose_name='Nbr de redouble'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='moyenneDiplome',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='moyenne diplome'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='moyenne_1_an',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='moyenne 1 année'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='moyenne_2_an',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True, verbose_name='moyenne 2 année'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='s1_an',
            field=models.CharField(max_length=10, verbose_name='Année S1'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='s2_an',
            field=models.CharField(max_length=10, verbose_name='Année S2'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='s3_an',
            field=models.CharField(max_length=10, verbose_name='Année S3'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='s4_an',
            field=models.CharField(max_length=10, verbose_name='Année S4'),
        ),
        migrations.AlterField(
            model_name='diplome',
            name='type_diplome_autre',
            field=models.CharField(blank=True, max_length=100, verbose_name='autre type de diplome'),
        ),
    ]