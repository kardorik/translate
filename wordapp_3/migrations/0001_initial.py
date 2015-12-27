# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pic_url', models.TextField(default=b'https://davidkallin.files.wordpress.com/2010/11/bart-simpson.jpg')),
                ('likes', models.IntegerField(default=0)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alien_description', models.TextField(default=b'')),
                ('native_description', models.TextField(default=b'')),
                ('likes', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=200)),
                ('definition', models.TextField(default=b'What does this word mean?')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='translation',
            name='alien_word',
            field=models.ForeignKey(related_name='alien_word', default=1, to='wordapp_3.Word'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='translation',
            name='native_word',
            field=models.ForeignKey(related_name='native_word', default=1, to='wordapp_3.Word'),
            preserve_default=True,
        ),
    ]
