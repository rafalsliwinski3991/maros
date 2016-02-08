# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0006_auto_20160126_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='taborup',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='taborup',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='taborup',
            name='image_t',
            field=models.ImageField(height_field='height_field', default='path/images', width_field='width_field', upload_to='tabor'),
        ),
    ]
