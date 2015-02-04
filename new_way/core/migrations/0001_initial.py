# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Accessory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('accessory', models.CharField(verbose_name='accessório', max_length=50)),
                ('price_accessory', models.DecimalField(verbose_name='preço', decimal_places=2, max_digits=8)),
            ],
            options={
                'ordering': ['accessory'],
                'verbose_name': 'accessório',
                'verbose_name_plural': 'accessórios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('address_number', models.PositiveIntegerField(verbose_name='número')),
                ('complement', models.CharField(verbose_name='complemento', max_length=80, blank=True)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(verbose_name='UF', max_length=2, choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')])),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
            ],
            options={
                'verbose_name': 'endereço',
                'verbose_name_plural': 'endereços',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(verbose_name='email', max_length=75, blank=True)),
                ('phone', models.CharField(verbose_name='telefone', max_length=15, blank=True)),
                ('cell', models.CharField(verbose_name='celular', max_length=15, blank=True)),
                ('address', models.ForeignKey(to='core.Address', verbose_name='endereço')),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('dealership', models.CharField(verbose_name='concessionária', max_length=50)),
                ('phone1', models.CharField(verbose_name='telefone 1', max_length=15, blank=True)),
                ('phone2', models.CharField(verbose_name='telefone 2', max_length=15, blank=True)),
                ('phone3', models.CharField(verbose_name='telefone 3', max_length=15, blank=True)),
                ('address', models.ForeignKey(to='core.Address', related_name='dealership_address', verbose_name='endereço')),
            ],
            options={
                'verbose_name': 'concessionária',
                'verbose_name_plural': 'concessionárias',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DealershipDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity_vehicle', models.PositiveIntegerField(verbose_name='quantidade')),
                ('dealership', models.ForeignKey(to='core.Dealership', related_name='dealership_det', verbose_name='concessionária')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(verbose_name='email', max_length=75, blank=True)),
                ('phone', models.CharField(verbose_name='telefone', max_length=15, blank=True)),
                ('cell', models.CharField(verbose_name='celular', max_length=15, blank=True)),
                ('comissioned', models.BooleanField(verbose_name='comissionado', default=True)),
                ('comission', models.DecimalField(verbose_name='comissão', decimal_places=2, max_digits=6)),
                ('address', models.ForeignKey(to='core.Address', verbose_name='endereço')),
                ('dealership', models.ForeignKey(to='core.Dealership', related_name='employee_dealership', verbose_name='concessionária')),
            ],
            options={
                'verbose_name': 'funcionário',
                'verbose_name_plural': 'funcionários',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('kiosk', models.CharField(verbose_name='quiosque', max_length=50)),
            ],
            options={
                'ordering': ['kiosk'],
                'verbose_name': 'quiosque',
                'verbose_name_plural': 'quiosques',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('kit', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['kit'],
                'verbose_name': 'kit',
                'verbose_name_plural': 'kits',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KitDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('quantity_accessory', models.PositiveIntegerField(verbose_name='quantidade')),
                ('accessory', models.ForeignKey(to='core.Accessory', related_name='accessory_kit', verbose_name='accessório')),
                ('kit', models.ForeignKey(to='core.Kit', related_name='kit_det', verbose_name='kit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('make', models.CharField(unique=True, verbose_name='marca', max_length=50)),
            ],
            options={
                'ordering': ['make'],
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('model', models.CharField(unique=True, verbose_name='modelo', max_length=50)),
                ('make', models.ForeignKey(to='core.Make', related_name='model_make', verbose_name='marca')),
            ],
            options={
                'ordering': ['model'],
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('occupation', models.CharField(verbose_name='cargo', max_length=50)),
            ],
            options={
                'verbose_name': 'cargo',
                'verbose_name_plural': 'cargos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('status', models.CharField(max_length=2, default='p', choices=[('c', 'cancelado'), ('p', 'pendente'), ('a', 'aprovado')])),
                ('customer', models.ForeignKey(to='core.Customer', verbose_name='cliente')),
                ('dealership', models.ForeignKey(to='core.Dealership', verbose_name='concessionária')),
                ('employee', models.ForeignKey(to='core.Employee', verbose_name='funcionário')),
                ('kiosk', models.ForeignKey(to='core.Kiosk', verbose_name='quiosque')),
                ('kit_optional', models.ForeignKey(to='core.Kit', verbose_name='kit opcional')),
            ],
            options={
                'ordering': ['-created_at'],
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('store', models.CharField(verbose_name='estabelecimento', max_length=50)),
                ('address', models.ForeignKey(to='core.Address', verbose_name='endereço')),
            ],
            options={
                'ordering': ['store'],
                'verbose_name': 'estabelecimento',
                'verbose_name_plural': 'estabelecimentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('vehicle', models.CharField(unique=True, verbose_name='veículo', max_length=50)),
                ('color', models.CharField(verbose_name='cor', max_length=50)),
                ('year_of_manufacture', models.PositiveIntegerField(verbose_name='ano de fabricação')),
                ('engine_power', models.DecimalField(verbose_name='potência do motor', decimal_places=2, max_digits=6)),
                ('fueltype', models.CharField(verbose_name='tipo de combustível', max_length=1, choices=[('g', 'gasolina'), ('a', 'álcool'), ('d', 'diesel'), ('f', 'flex'), ('e', 'elétrico')])),
                ('transmissiontype', models.CharField(verbose_name='tipo de câmbio', max_length=1, choices=[('a', 'automático'), ('m', 'manual')])),
                ('wheel', models.CharField(verbose_name='freio', max_length=30)),
                ('tire', models.CharField(verbose_name='roda', max_length=30)),
                ('performance', models.CharField(verbose_name='desempenho', max_length=30)),
                ('trunk', models.CharField(verbose_name='porta malas', max_length=30)),
                ('price', models.DecimalField(verbose_name='preço', decimal_places=2, max_digits=8)),
                ('kit_fabric', models.ForeignKey(to='core.Kit', related_name='vehicle_kit', verbose_name='kit de fábrica')),
                ('model', models.ForeignKey(to='core.Model', related_name='vehicle_model', verbose_name='modelo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ordered',
            name='vehicle',
            field=models.ForeignKey(to='core.Vehicle', verbose_name='veículo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kiosk',
            name='store',
            field=models.ForeignKey(to='core.Store', related_name='kiosk_store', verbose_name='quiosque'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(to='core.Occupation', related_name='employee_occupation', verbose_name='cargo'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dealershipdetail',
            name='vehicle',
            field=models.ForeignKey(to='core.Vehicle', related_name='vehicle_det', verbose_name='veículo'),
            preserve_default=True,
        ),
    ]
