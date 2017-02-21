# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_productmodel_categorypk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='categoryPK',
        ),
    ]
