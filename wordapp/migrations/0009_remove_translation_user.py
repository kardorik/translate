# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0008_auto_20151225_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='user',
        ),
    ]
