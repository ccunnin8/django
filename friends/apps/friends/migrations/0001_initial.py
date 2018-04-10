# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-06 00:32
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
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friender', to='users.User')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendee', to='users.User')),
            ],
        ),
    ]
