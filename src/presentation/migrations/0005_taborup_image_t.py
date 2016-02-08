# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0004_taborup'),
    ]

    operations = [
        migrations.AddField(
            model_name='taborup',
            name='image_t',
            field=models.ImageField(upload_to='tabor', default='path/images'),
        ),
    ]
