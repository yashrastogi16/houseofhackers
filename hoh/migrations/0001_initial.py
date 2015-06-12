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
                ('dob', models.CharField(max_length=60, verbose_name=b'Date Of Birth')),
                ('location', models.CharField(max_length=60, verbose_name=b'Location')),
                ('email_id', models.EmailField(max_length=60, verbose_name=b'Email')),
                ('self_description', models.TextField()),
                ('achievements', models.TextField()),
                ('project_name', models.CharField(max_length=60, verbose_name=b'Project Name')),
                ('project_link', models.URLField(max_length=255, verbose_name=b'Project Link')),
                ('project_Description', models.TextField()),
                ('skills_used', models.TextField()),
                ('date_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
