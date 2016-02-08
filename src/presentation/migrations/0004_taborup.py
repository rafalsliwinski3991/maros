# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('presentation', '0003_auto_20160122_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaborUp',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('machine', models.CharField(max_length=200)),
            ],
        ),
    ]
