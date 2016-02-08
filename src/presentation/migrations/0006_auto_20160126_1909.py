# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0005_taborup_image_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taborup',
            name='image_t',
            field=models.ImageField(height_field='300', upload_to='tabor', default='path/images', width_field='500'),
        ),
    ]
