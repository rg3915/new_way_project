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
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('accessory', models.CharField(verbose_name='accessório', max_length=50)),
                ('price_accessory', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='preço')),
                ('photo_accessory', models.ImageField(upload_to='accessorys', null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'accessórios',
                'ordering': ['accessory'],
                'verbose_name': 'accessório',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('brand', models.CharField(unique=True, verbose_name='marca', max_length=50)),
                ('photo', models.ImageField(upload_to='brands')),
            ],
            options={
                'verbose_name_plural': 'marcas',
                'ordering': ['brand'],
                'verbose_name': 'marca',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('complement', models.CharField(null=True, verbose_name='complemento', blank=True, max_length=80)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], verbose_name='gênero', max_length=1)),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(verbose_name='email', blank=True, max_length=75)),
                ('phone', models.CharField(null=True, verbose_name='telefone', blank=True, max_length=15)),
                ('cell', models.CharField(null=True, verbose_name='celular', blank=True, max_length=15)),
            ],
            options={
                'verbose_name_plural': 'clientes',
                'verbose_name': 'cliente',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dealership',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('complement', models.CharField(null=True, verbose_name='complemento', blank=True, max_length=80)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('dealership', models.CharField(verbose_name='concessionária', max_length=50)),
                ('site', models.CharField(null=True, verbose_name='site', blank=True, max_length=100)),
                ('phone1', models.CharField(null=True, verbose_name='telefone 1', blank=True, max_length=15)),
                ('phone2', models.CharField(null=True, verbose_name='telefone 2', blank=True, max_length=15)),
                ('phone3', models.CharField(null=True, verbose_name='telefone 3', blank=True, max_length=15)),
            ],
            options={
                'verbose_name_plural': 'concessionárias',
                'verbose_name': 'concessionária',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DealershipDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantity_vehicle', models.PositiveIntegerField(verbose_name='quantidade')),
                ('dealership', models.ForeignKey(related_name='dealership_det', to='core.Dealership', verbose_name='concessionária')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('complement', models.CharField(null=True, verbose_name='complemento', blank=True, max_length=80)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], verbose_name='gênero', max_length=1)),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(unique=True, verbose_name='CPF', max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(verbose_name='email', blank=True, max_length=75)),
                ('phone', models.CharField(null=True, verbose_name='telefone', blank=True, max_length=15)),
                ('cell', models.CharField(null=True, verbose_name='celular', blank=True, max_length=15)),
                ('comissioned', models.BooleanField(verbose_name='comissionado', default=True)),
                ('comission', models.DecimalField(max_digits=6, decimal_places=2, verbose_name='comissão')),
                ('dealership', models.ForeignKey(related_name='employee_dealership', to='core.Dealership', verbose_name='concessionária')),
            ],
            options={
                'verbose_name_plural': 'funcionários',
                'verbose_name': 'funcionário',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kiosk',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('kiosk', models.CharField(verbose_name='quiosque', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'quiosques',
                'ordering': ['kiosk'],
                'verbose_name': 'quiosque',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('kit', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'kits',
                'ordering': ['kit'],
                'verbose_name': 'kit',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KitDetail',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('quantity_accessory', models.PositiveIntegerField(verbose_name='quantidade')),
                ('accessory', models.ForeignKey(related_name='accessory_kit', to='core.Accessory', verbose_name='accessório')),
                ('kit', models.ForeignKey(related_name='kit_det', to='core.Kit', verbose_name='kit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modell',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('modell', models.CharField(unique=True, verbose_name='modelo', max_length=50)),
                ('brand', models.ForeignKey(related_name='model_brand', to='core.Brand', verbose_name='marca')),
            ],
            options={
                'verbose_name_plural': 'modelos',
                'ordering': ['modell'],
                'verbose_name': 'modelo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('occupation', models.CharField(verbose_name='cargo', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'cargos',
                'verbose_name': 'cargo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('status', models.CharField(choices=[('c', 'cancelado'), ('p', 'pendente'), ('a', 'aprovado')], default='p', max_length=2)),
                ('customer', models.ForeignKey(to='core.Customer', verbose_name='cliente')),
                ('dealership', models.ForeignKey(to='core.Dealership', verbose_name='concessionária')),
                ('kiosk', models.ForeignKey(to='core.Kiosk', verbose_name='quiosque')),
                ('kit_optional', models.ForeignKey(to='core.Kit', verbose_name='kit opcional')),
            ],
            options={
                'verbose_name_plural': 'pedidos',
                'ordering': ['-id'],
                'verbose_name': 'pedido',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('store', models.CharField(verbose_name='estabelecimento', max_length=65)),
                ('phone', models.CharField(verbose_name='telefone', blank=True, max_length=15)),
                ('city', models.CharField(verbose_name='cidade', blank=True, max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
            ],
            options={
                'verbose_name_plural': 'estabelecimentos',
                'ordering': ['store'],
                'verbose_name': 'estabelecimento',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('vehicle', models.CharField(unique=True, verbose_name='veículo', max_length=50)),
                ('color', models.CharField(verbose_name='cor', max_length=50)),
                ('year_of_manufacture', models.PositiveIntegerField(verbose_name='ano de fabricação')),
                ('engine_power', models.DecimalField(max_digits=6, decimal_places=2, verbose_name='motor')),
                ('fueltype', models.CharField(choices=[('g', 'gasolina'), ('a', 'álcool'), ('d', 'diesel'), ('f', 'flex'), ('e', 'elétrico')], verbose_name='tipo de combustível', max_length=1)),
                ('transmissiontype', models.CharField(choices=[('a', 'automático'), ('m', 'manual')], verbose_name='tipo de câmbio', max_length=1)),
                ('power', models.CharField(default='-', verbose_name='potência', max_length=30)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2, verbose_name='preço')),
                ('photo_vehicle', models.ImageField(upload_to='vehicles', default='vehicles/car_700x300.jpg')),
                ('kit_fabric', models.ForeignKey(related_name='vehicle_kit', to='core.Kit', verbose_name='kit de fábrica')),
                ('modell', models.ForeignKey(related_name='vehicle_model', to='core.Modell', verbose_name='modelo')),
            ],
            options={
                'verbose_name_plural': 'veículos',
                'ordering': ['vehicle'],
                'verbose_name': 'veículo',
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
            field=models.ForeignKey(related_name='kiosk_store', to='core.Store', verbose_name='estabelecimento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(related_name='employee_occupation', to='core.Occupation', verbose_name='cargo'),
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
            field=models.ForeignKey(related_name='vehicle_det', to='core.Vehicle', verbose_name='veículo'),
            preserve_default=True,
        ),
    ]
