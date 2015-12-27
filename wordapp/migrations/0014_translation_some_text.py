# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0013_remove_translation_some_integer'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='some_text',
            field=models.CharField(default=b'something', max_length=200),
            preserve_default=True,
        ),
    ]
