# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0002_auto_20151225_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='author',
        ),
    ]
