# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-26 20:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'P'), ('Complete', 'C'), ('Missed', 'M')], default='P', max_length=15),
        ),
    ]
