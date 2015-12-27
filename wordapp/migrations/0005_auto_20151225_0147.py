# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0004_profiledebug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiledebug',
            name='user',
        ),
        migrations.DeleteModel(
            name='ProfileDebug',
        ),
    ]
