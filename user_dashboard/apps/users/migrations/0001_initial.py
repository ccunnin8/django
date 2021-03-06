# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-22 13:06
from __future__ import unicode_literals

import apps.users.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('last_name', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255, validators=[apps.users.models.password_validation])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('admin', models.BooleanField(default=False)),
            ],
        ),
    ]
