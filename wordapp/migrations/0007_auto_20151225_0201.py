# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0006_translation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='user',
            field=models.OneToOneField(default=1, to='wordapp.Profile'),
            preserve_default=True,
        ),
    ]
