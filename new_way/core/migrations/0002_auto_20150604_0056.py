# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cell',
            field=models.CharField(blank=True, verbose_name='celular', max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, verbose_name='telefone', max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employee',
            name='cell',
            field=models.CharField(blank=True, verbose_name='celular', max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, verbose_name='telefone', max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='store',
            name='store',
            field=models.CharField(verbose_name='estabelecimento', max_length=65),
            preserve_default=True,
        ),
    ]
