# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_buyevent_externalurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buyevent',
            old_name='model_pic',
            new_name='photo',
        ),
    ]
