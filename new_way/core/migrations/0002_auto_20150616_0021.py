# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='dealership',
            field=models.ManyToManyField(to='core.Dealership', verbose_name='concessionária'),
            preserve_default=True,
        ),
    ]
