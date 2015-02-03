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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('accessory', models.CharField(verbose_name='accessório', max_length=50)),
                ('price_accessory', models.DecimalField(verbose_name='preço', max_digits=8, decimal_places=2)),
            ],
            options={
                'verbose_name': 'accessório',
                'verbose_name_plural': 'accessórios',
                'ordering': ['accessory'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('address_number', models.PositiveIntegerField(verbose_name='número')),
                ('complement', models.CharField(verbose_name='complemento', blank=True, max_length=80)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(verbose_name='email', blank=True, max_length=75)),
                ('phone', models.CharField(verbose_name='telefone', blank=True, max_length=15)),
                ('cell', models.CharField(verbose_name='celular', blank=True, max_length=15)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('dealership', models.CharField(verbose_name='concessionária', max_length=50)),
                ('phone1', models.CharField(verbose_name='telefone 1', blank=True, max_length=15)),
                ('phone2', models.CharField(verbose_name='telefone 2', blank=True, max_length=15)),
                ('phone3', models.CharField(verbose_name='telefone 3', blank=True, max_length=15)),
                ('address', models.ForeignKey(related_name='dealership_address', to='core.Address', verbose_name='endereço')),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quantity_vehicle', models.PositiveIntegerField(verbose_name='quantidade')),
                ('dealership', models.ForeignKey(related_name='dealership_det', to='core.Dealership', verbose_name='concessionária')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('kiosk', models.CharField(verbose_name='quiosque', max_length=50)),
            ],
            options={
                'verbose_name': 'quiosque',
                'verbose_name_plural': 'quiosques',
                'ordering': ['kiosk'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('kit', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'kit',
                'verbose_name_plural': 'kits',
                'ordering': ['kit'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KitDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('quantity_accessory', models.PositiveIntegerField(verbose_name='quantidade')),
                ('accessory', models.ForeignKey(related_name='accessory_kit', to='core.Accessory', verbose_name='accessório')),
                ('kit', models.ForeignKey(related_name='kit_det', to='core.Kit', verbose_name='kit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('make', models.CharField(unique=True, verbose_name='marca', max_length=50)),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['make'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('model', models.CharField(unique=True, verbose_name='modelo', max_length=50)),
                ('make', models.ForeignKey(related_name='model_make', to='core.Make', verbose_name='marca')),
            ],
            options={
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelos',
                'ordering': ['model'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('status', models.CharField(default='p', max_length=2, choices=[('c', 'cancelado'), ('p', 'pendente'), ('a', 'aprovado')])),
                ('customer', models.ForeignKey(to='core.Customer', verbose_name='cliente')),
                ('dealership', models.ForeignKey(to='core.Dealership', verbose_name='concessionária')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
                'ordering': ['-created_at'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('store', models.CharField(verbose_name='estabelecimento', max_length=50)),
                ('address', models.ForeignKey(to='core.Address', verbose_name='endereço')),
            ],
            options={
                'verbose_name': 'estabelecimento',
                'verbose_name_plural': 'estabelecimentos',
                'ordering': ['store'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('userprofile_ptr', models.OneToOneField(to='core.UserProfile', serialize=False, auto_created=True, parent_link=True, primary_key=True)),
                ('comissioned', models.BooleanField(default=True, verbose_name='comissionado')),
                ('comission', models.DecimalField(verbose_name='comissão', max_digits=6, decimal_places=2)),
                ('dealership', models.ForeignKey(related_name='employee_dealership', to='core.Dealership', verbose_name='concessionária')),
                ('occupation', models.ForeignKey(related_name='employee_occupation', to='core.Occupation', verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'funcionário',
                'verbose_name_plural': 'funcionários',
            },
            bases=('core.userprofile',),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('vehicle', models.CharField(unique=True, verbose_name='veículo', max_length=50)),
                ('color', models.CharField(verbose_name='cor', max_length=50)),
                ('year_of_manufacture', models.PositiveIntegerField(verbose_name='ano de fabricação')),
                ('engine_power', models.DecimalField(verbose_name='potência do motor', max_digits=6, decimal_places=2)),
                ('fueltype', models.CharField(verbose_name='tipo de combustível', max_length=1, choices=[('g', 'gasolina'), ('a', 'álcool'), ('d', 'diesel'), ('f', 'flex'), ('e', 'elétrico')])),
                ('transmissiontype', models.CharField(verbose_name='tipo de câmbio', max_length=1, choices=[('a', 'automático'), ('m', 'manual')])),
                ('wheel', models.CharField(verbose_name='freio', max_length=30)),
                ('tire', models.CharField(verbose_name='roda', max_length=30)),
                ('performance', models.CharField(verbose_name='desempenho', max_length=30)),
                ('trunk', models.CharField(verbose_name='porta malas', max_length=30)),
                ('price', models.DecimalField(verbose_name='preço', max_digits=8, decimal_places=2)),
                ('kit_fabric', models.ForeignKey(related_name='vehicle_kit', to='core.Kit', verbose_name='kit de fábrica')),
                ('model', models.ForeignKey(related_name='vehicle_model', to='core.Model', verbose_name='modelo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordered',
            name='employee',
            field=models.ForeignKey(to='core.Employee', verbose_name='funcionário'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordered',
            name='kiosk',
            field=models.ForeignKey(to='core.Kiosk', verbose_name='quiosque'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ordered',
            name='kit_optional',
            field=models.ForeignKey(to='core.Kit', verbose_name='kit opcional'),
            preserve_default=True,
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
            field=models.ForeignKey(related_name='kiosk_store', to='core.Store', verbose_name='quiosque'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dealershipdetail',
            name='vehicle',
            field=models.ForeignKey(related_name='vehicle_det', to='core.Vehicle', verbose_name='veículo'),
            preserve_default=True,
        ),
    ]
