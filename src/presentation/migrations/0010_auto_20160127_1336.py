# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0009_auto_20160127_1334'),
    ]

    operations = [
        migrations.RenameField(
            model_name='refmod',
            old_name='image_t',
            new_name='image_r',
        ),
        migrations.RenameField(
            model_name='refmod',
            old_name='machine',
            new_name='name',
        ),
    ]
