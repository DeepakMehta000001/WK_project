# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='Product_name',
            new_name='product_name',
        ),
    ]