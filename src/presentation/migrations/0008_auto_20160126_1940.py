# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0007_auto_20160126_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taborup',
            name='image_t',
            field=models.ImageField(width_field='width_field', height_field='height_field', upload_to='tabor'),
        ),
    ]
