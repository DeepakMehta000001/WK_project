# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('categoryPK', models.ForeignKey(to='category.CategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('subcategory_name', models.CharField(max_length=50)),
                ('categoryPK', models.ForeignKey(to='category.CategoryModel')),
            ],
        ),
        migrations.AddField(
            model_name='productmodel',
            name='subcategoryPK',
            field=models.ForeignKey(to='category.SubCategoryModel'),
        ),
    ]
