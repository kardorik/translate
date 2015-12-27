# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp', '0005_auto_20151225_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='user',
            field=models.OneToOneField(null=True, to='wordapp.Profile'),
            preserve_default=True,
        ),
    ]
