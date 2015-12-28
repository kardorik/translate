# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp_3', '0003_auto_20151227_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='native_translation_word',
            field=models.ForeignKey(related_name='native_translation_word', default=1, to='wordapp_3.Word'),
            preserve_default=True,
        ),
    ]
