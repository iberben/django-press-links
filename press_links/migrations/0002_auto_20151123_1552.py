# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('source', models.CharField(max_length=255, verbose_name='the source for the entry', blank=True)),
                ('excerpt', models.TextField(verbose_name='Excerpt', blank=True)),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='press_links.Entry', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'press_links_entry_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Press Entry Translation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkTranslation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_code', models.CharField(max_length=15, verbose_name='Language', db_index=True)),
                ('link', models.CharField(max_length=255, verbose_name='link address (add http:// for external link)')),
                ('link_text', models.CharField(max_length=255, verbose_name='text for link')),
                ('master', models.ForeignKey(related_name='translations', editable=False, to='press_links.Link', null=True)),
            ],
            options={
                'managed': True,
                'db_table': 'press_links_link_translation',
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'Press Link Translation',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='linktranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='entrytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.RemoveField(
            model_name='entry',
            name='excerpt',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='source',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='title',
        ),
        migrations.RemoveField(
            model_name='link',
            name='link',
        ),
        migrations.RemoveField(
            model_name='link',
            name='link_text',
        ),
    ]
