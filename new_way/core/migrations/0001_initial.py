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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('accessory', models.CharField(verbose_name='accessório', max_length=50)),
                ('price_accessory', models.DecimalField(verbose_name='preço', decimal_places=2, max_digits=8)),
                ('photo_accessory', models.ImageField(blank=True, upload_to='accessorys', null=True)),
            ],
            options={
                'verbose_name': 'accessório',
                'verbose_name_plural': 'accessórios',
                'ordering': ['accessory'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('brand', models.CharField(verbose_name='marca', unique=True, max_length=50)),
                ('photo', models.ImageField(upload_to='brands')),
            ],
            options={
                'verbose_name': 'marca',
                'verbose_name_plural': 'marcas',
                'ordering': ['brand'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('complement', models.CharField(blank=True, verbose_name='complemento', null=True, max_length=80)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], verbose_name='gênero', max_length=1)),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(verbose_name='CPF', unique=True, max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(blank=True, verbose_name='email', max_length=75)),
                ('phone', models.CharField(blank=True, verbose_name='telefone', null=True, max_length=15)),
                ('cell', models.CharField(blank=True, verbose_name='celular', null=True, max_length=15)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('complement', models.CharField(blank=True, verbose_name='complemento', null=True, max_length=80)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('dealership', models.CharField(verbose_name='concessionária', max_length=50)),
                ('site', models.CharField(blank=True, verbose_name='site', null=True, max_length=100)),
                ('phone1', models.CharField(blank=True, verbose_name='telefone 1', null=True, max_length=15)),
                ('phone2', models.CharField(blank=True, verbose_name='telefone 2', null=True, max_length=15)),
                ('phone3', models.CharField(blank=True, verbose_name='telefone 3', null=True, max_length=15)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity_vehicle', models.PositiveIntegerField(verbose_name='quantidade')),
                ('dealership', models.ForeignKey(verbose_name='concessionária', related_name='dealership_det', to='core.Dealership')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('address', models.CharField(verbose_name='endereço', max_length=80)),
                ('complement', models.CharField(blank=True, verbose_name='complemento', null=True, max_length=80)),
                ('district', models.CharField(verbose_name='bairro', max_length=80)),
                ('city', models.CharField(verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
                ('cep', models.CharField(verbose_name='CEP', max_length=9)),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], verbose_name='gênero', max_length=1)),
                ('first_name', models.CharField(verbose_name='nome', max_length=100)),
                ('last_name', models.CharField(verbose_name='sobrenome', max_length=100)),
                ('cpf', models.CharField(verbose_name='CPF', unique=True, max_length=11)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(blank=True, verbose_name='email', max_length=75)),
                ('phone', models.CharField(blank=True, verbose_name='telefone', null=True, max_length=15)),
                ('cell', models.CharField(blank=True, verbose_name='celular', null=True, max_length=15)),
                ('comissioned', models.BooleanField(verbose_name='comissionado', default=True)),
                ('comission', models.DecimalField(verbose_name='comissão', decimal_places=2, max_digits=6)),
                ('dealership', models.ForeignKey(verbose_name='concessionária', related_name='employee_dealership', to='core.Dealership')),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('quantity_accessory', models.PositiveIntegerField(verbose_name='quantidade')),
                ('accessory', models.ForeignKey(verbose_name='accessório', related_name='accessory_kit', to='core.Accessory')),
                ('kit', models.ForeignKey(verbose_name='kit', related_name='kit_det', to='core.Kit')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modell',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('modell', models.CharField(verbose_name='modelo', unique=True, max_length=50)),
                ('brand', models.ForeignKey(verbose_name='marca', related_name='model_brand', to='core.Brand')),
            ],
            options={
                'verbose_name': 'modelo',
                'verbose_name_plural': 'modelos',
                'ordering': ['modell'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modificado em')),
                ('status', models.CharField(choices=[('c', 'cancelado'), ('p', 'pendente'), ('a', 'aprovado')], max_length=2, default='p')),
                ('customer', models.ForeignKey(verbose_name='cliente', to='core.Customer')),
                ('dealership', models.ManyToManyField(to='core.Dealership')),
                ('kiosk', models.ForeignKey(verbose_name='quiosque', to='core.Kiosk')),
                ('kit_optional', models.ForeignKey(verbose_name='kit opcional', to='core.Kit')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
                'ordering': ['-id'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('store', models.CharField(verbose_name='estabelecimento', max_length=65)),
                ('phone', models.CharField(blank=True, verbose_name='telefone', max_length=15)),
                ('city', models.CharField(blank=True, verbose_name='cidade', max_length=80)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], verbose_name='UF', max_length=2)),
            ],
            options={
                'verbose_name': 'estabelecimento',
                'verbose_name_plural': 'estabelecimentos',
                'ordering': ['store'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('vehicle', models.CharField(verbose_name='veículo', unique=True, max_length=50)),
                ('color', models.CharField(verbose_name='cor', max_length=50)),
                ('year_of_manufacture', models.PositiveIntegerField(verbose_name='ano de fabricação')),
                ('engine_power', models.DecimalField(verbose_name='motor', decimal_places=2, max_digits=6)),
                ('fueltype', models.CharField(choices=[('g', 'gasolina'), ('a', 'álcool'), ('d', 'diesel'), ('f', 'flex'), ('e', 'elétrico')], verbose_name='tipo de combustível', max_length=1)),
                ('transmissiontype', models.CharField(choices=[('a', 'automático'), ('m', 'manual')], verbose_name='tipo de câmbio', max_length=1)),
                ('power', models.CharField(verbose_name='potência', default='-', max_length=30)),
                ('price', models.DecimalField(verbose_name='preço', decimal_places=2, max_digits=8)),
                ('photo_vehicle', models.ImageField(upload_to='vehicles', default='vehicles/car_700x300.jpg')),
                ('kit_fabric', models.ForeignKey(verbose_name='kit de fábrica', related_name='vehicle_kit', to='core.Kit')),
                ('modell', models.ForeignKey(verbose_name='modelo', related_name='vehicle_model', to='core.Modell')),
            ],
            options={
                'verbose_name': 'veículo',
                'verbose_name_plural': 'veículos',
                'ordering': ['vehicle'],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ordered',
            name='vehicle',
            field=models.ForeignKey(verbose_name='veículo', to='core.Vehicle'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='kiosk',
            name='store',
            field=models.ForeignKey(verbose_name='estabelecimento', related_name='kiosk_store', to='core.Store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(verbose_name='cargo', related_name='employee_occupation', to='core.Occupation'),
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
            field=models.ForeignKey(verbose_name='veículo', related_name='vehicle_det', to='core.Vehicle'),
            preserve_default=True,
        ),
    ]
