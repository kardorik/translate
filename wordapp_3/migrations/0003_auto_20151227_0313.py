# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wordapp_3', '0002_translation_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='translation',
            name='pic_url',
            field=models.TextField(default=b'http://s.hswstatic.com/gif/electric-car-history-2.jpg'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic_url',
            field=models.TextField(default=b'https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcT0mp4SuvY1YNtjFXIk7YFjT42HLjN_tpLOjnUX9dvAaSFO1jbsEQ'),
            preserve_default=True,
        ),
    ]
