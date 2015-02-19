# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User123',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('hours_needed', models.PositiveIntegerField(default=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
