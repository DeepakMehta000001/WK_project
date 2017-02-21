# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20170220_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='categoryPK',
            field=models.ForeignKey(default=datetime.datetime(2017, 2, 21, 8, 37, 2, 26941, tzinfo=utc), to='category.CategoryModel'),
            preserve_default=False,
        ),
    ]
