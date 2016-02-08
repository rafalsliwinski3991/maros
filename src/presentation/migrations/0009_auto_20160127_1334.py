# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('presentation', '0008_auto_20160126_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postmod',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Refmod',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('machine', models.CharField(max_length=200)),
                ('image_t', models.ImageField(width_field='width_field', upload_to='referencje', height_field='height_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='TaborUp',
            new_name='Tabormod',
        ),
        migrations.RemoveField(
            model_name='postup',
            name='author',
        ),
        migrations.DeleteModel(
            name='PostUp',
        ),
    ]
