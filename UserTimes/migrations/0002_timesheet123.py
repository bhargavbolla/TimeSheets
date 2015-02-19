# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserTimes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSheet123',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_worked', models.DateField(default=b'2014-02-02')),
                ('time_from', models.TimeField(default=b'10:15:20')),
                ('time_to', models.TimeField(default=b'10:15:20')),
                ('time_total', models.DecimalField(default=0, max_digits=5, decimal_places=2)),
                ('user', models.ForeignKey(to='UserTimes.User123')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
