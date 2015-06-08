# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20150607_0322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='kit_optional',
            field=models.ForeignKey(verbose_name='kit opcional', to='core.Kit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='kit_fabric',
            field=models.ForeignKey(to='core.Kit', related_name='vehicle_kit', verbose_name='kit de fábrica'),
            preserve_default=True,
        ),
    ]
