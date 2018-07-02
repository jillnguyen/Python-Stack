# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='liked_users',
            field=models.ManyToManyField(null=True, related_name='liked_books', to='likes.User'),
        ),
        migrations.AlterField(
            model_name='book',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_books', to='likes.User'),
        ),
    ]
