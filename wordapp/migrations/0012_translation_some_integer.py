# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0011_auto_20151227_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='some_integer',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
