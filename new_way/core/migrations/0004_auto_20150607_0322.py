# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150607_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='kit_optional',
            field=models.ForeignKey(to='core.KitDetail', verbose_name='kit opcional'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='kit_fabric',
            field=models.ForeignKey(related_name='vehicle_kit', verbose_name='kit de fábrica', to='core.KitDetail'),
            preserve_default=True,
        ),
    ]
