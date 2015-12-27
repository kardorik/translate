# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0012_translation_some_integer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='translation',
            name='some_integer',
        ),
    ]
