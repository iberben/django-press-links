# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, verbose_name=b'slug', unique_for_date=b'pub_date')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publication date')),
                ('status', models.IntegerField(default=2, verbose_name='status', choices=[(1, 'Live'), (2, 'Draft'), (3, 'Hidden')])),
                ('excerpt', models.TextField(verbose_name='Excerpt', blank=True)),
                ('source', models.CharField(max_length=255, verbose_name='the source for the entry', blank=True)),
                ('author', models.ForeignKey(related_name='press_links_entry_related', verbose_name='author', to=settings.AUTH_USER_MODEL)),
                ('site', models.ManyToManyField(related_name='press_links_entry_related', verbose_name='Sites where the entry is published', to='sites.Site')),
            ],
            options={
                'ordering': ['-pub_date'],
                'get_latest_by': 'pub_date',
                'verbose_name': 'Press Entry',
                'verbose_name_plural': 'Press Entries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link', models.CharField(max_length=255, verbose_name='link address (add http:// for external link)')),
                ('link_text', models.CharField(max_length=255, verbose_name='text for link')),
                ('link_new_page', models.BooleanField(default=False, verbose_name='open link in new page')),
                ('entry', models.ForeignKey(verbose_name='Entry', to='press_links.Entry')),
            ],
            options={
                'verbose_name': 'Press Link',
                'verbose_name_plural': 'Press Links',
            },
            bases=(models.Model,),
        ),
    ]
