# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150604_0056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordered',
            options={'verbose_name_plural': 'pedidos', 'ordering': ['-id'], 'verbose_name': 'pedido'},
        ),
        migrations.AddField(
            model_name='accessory',
            name='photo_accessory',
            field=models.ImageField(null=True, upload_to='accessorys', blank=True),
            preserve_default=True,
        ),
    ]
