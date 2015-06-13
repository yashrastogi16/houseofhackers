# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contestant_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('university', models.CharField(max_length=60, verbose_name=b'University')),
                ('username', models.CharField(max_length=60, verbose_name=b'Name')),
                ('link_stockroom', models.CharField(max_length=255, verbose_name=b'Link_Stockroom')),
                ('location', models.CharField(max_length=60, verbose_name=b'Location')),
                ('email_id', models.EmailField(max_length=60, verbose_name=b'Email')),
                ('self_description', models.TextField()),
                ('achievements', models.TextField()),
                ('project', models.TextField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=60, verbose_name=b'Name')),
                ('email_id', models.EmailField(max_length=255, verbose_name=b'Email')),
                ('query', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
