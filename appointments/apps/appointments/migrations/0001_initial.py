# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-18 14:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasks', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('P', 'Pending'), ('C', 'Complete'), ('M', 'Missed')], default='P', max_length=15)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='users.User')),
            ],
        ),
    ]
