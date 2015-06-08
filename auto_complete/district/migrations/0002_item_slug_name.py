# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug_name',
            field=models.SlugField(default='test', max_length=300),
            preserve_default=False,
        ),
    ]
