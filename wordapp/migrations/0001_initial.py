# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('english_text', models.CharField(max_length=200)),
                ('italian_text', models.CharField(max_length=200)),
                ('english_description', models.TextField()),
                ('italian_description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
