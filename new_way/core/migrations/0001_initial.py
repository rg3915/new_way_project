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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('accessory', models.CharField(max_length=50, verbose_name='accessório')),
                ('price_accessory', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço')),
            ],
            options={
                'verbose_name': 'accessório',
                'ordering': ['accessory'],
                'verbose_name_plural': 'accessórios',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('brand', models.CharField(max_length=50, verbose_name='marca', unique=True)),
                ('photo', models.ImageField(upload_to='brands')),
            ],
            options={
                'verbose_name': 'marca',
                'ordering': ['brand'],
                'verbose_name_plural': 'marcas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('address', models.CharField(max_length=80, verbose_name='endereço')),
                ('complement', models.CharField(null=True, blank=True, max_length=80, verbose_name='complemento')),
                ('district', models.CharField(max_length=80, verbose_name='bairro')),
                ('city', models.CharField(max_length=80, verbose_name='cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, verbose_name='gênero')),
                ('first_name', models.CharField(max_length=100, verbose_name='nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='sobrenome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF', unique=True)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('cell', models.CharField(blank=True, max_length=15, verbose_name='celular')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('address', models.CharField(max_length=80, verbose_name='endereço')),
                ('complement', models.CharField(null=True, blank=True, max_length=80, verbose_name='complemento')),
                ('district', models.CharField(max_length=80, verbose_name='bairro')),
                ('city', models.CharField(max_length=80, verbose_name='cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('dealership', models.CharField(max_length=50, verbose_name='concessionária')),
                ('site', models.CharField(null=True, blank=True, max_length=100, verbose_name='site')),
                ('phone1', models.CharField(null=True, blank=True, max_length=15, verbose_name='telefone 1')),
                ('phone2', models.CharField(null=True, blank=True, max_length=15, verbose_name='telefone 2')),
                ('phone3', models.CharField(null=True, blank=True, max_length=15, verbose_name='telefone 3')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quantity_vehicle', models.PositiveIntegerField(verbose_name='quantidade')),
                ('dealership', models.ForeignKey(verbose_name='concessionária', to='core.Dealership', related_name='dealership_det')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('address', models.CharField(max_length=80, verbose_name='endereço')),
                ('complement', models.CharField(null=True, blank=True, max_length=80, verbose_name='complemento')),
                ('district', models.CharField(max_length=80, verbose_name='bairro')),
                ('city', models.CharField(max_length=80, verbose_name='cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('gender', models.CharField(choices=[('M', 'masculino'), ('F', 'feminino')], max_length=1, verbose_name='gênero')),
                ('first_name', models.CharField(max_length=100, verbose_name='nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='sobrenome')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF', unique=True)),
                ('birthday', models.DateField(verbose_name='data de nascimento')),
                ('email', models.EmailField(blank=True, max_length=75, verbose_name='email')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('cell', models.CharField(blank=True, max_length=15, verbose_name='celular')),
                ('comissioned', models.BooleanField(default=True, verbose_name='comissionado')),
                ('comission', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='comissão')),
                ('dealership', models.ForeignKey(verbose_name='concessionária', to='core.Dealership', related_name='employee_dealership')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('kiosk', models.CharField(max_length=50, verbose_name='quiosque')),
            ],
            options={
                'verbose_name': 'quiosque',
                'ordering': ['kiosk'],
                'verbose_name_plural': 'quiosques',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Kit',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('kit', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'kit',
                'ordering': ['kit'],
                'verbose_name_plural': 'kits',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KitDetail',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('quantity_accessory', models.PositiveIntegerField(verbose_name='quantidade')),
                ('accessory', models.ForeignKey(verbose_name='accessório', to='core.Accessory', related_name='accessory_kit')),
                ('kit', models.ForeignKey(verbose_name='kit', to='core.Kit', related_name='kit_det')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modell',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('modell', models.CharField(max_length=50, verbose_name='modelo', unique=True)),
                ('brand', models.ForeignKey(verbose_name='marca', to='core.Brand', related_name='model_brand')),
            ],
            options={
                'verbose_name': 'modelo',
                'ordering': ['modell'],
                'verbose_name_plural': 'modelos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('occupation', models.CharField(max_length=50, verbose_name='cargo')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(verbose_name='criado em', auto_now_add=True)),
                ('modified_at', models.DateTimeField(verbose_name='modificado em', auto_now=True)),
                ('status', models.CharField(default='p', max_length=2, choices=[('c', 'cancelado'), ('p', 'pendente'), ('a', 'aprovado')])),
                ('customer', models.ForeignKey(verbose_name='cliente', to='core.Customer')),
                ('dealership', models.ForeignKey(verbose_name='concessionária', to='core.Dealership')),
                ('employee', models.ForeignKey(verbose_name='funcionário', to='core.Employee')),
                ('kiosk', models.ForeignKey(verbose_name='quiosque', to='core.Kiosk')),
                ('kit_optional', models.ForeignKey(verbose_name='kit opcional', to='core.Kit')),
            ],
            options={
                'verbose_name': 'pedido',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'pedidos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('store', models.CharField(max_length=50, verbose_name='estabelecimento')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='telefone')),
                ('city', models.CharField(blank=True, max_length=80, verbose_name='cidade')),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AM', 'Amazonas'), ('AP', 'Amapá'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Brasília'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MG', 'Minas Gerais'), ('MS', 'Mato Grosso do Sul'), ('MT', 'Mato Grosso'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('PR', 'Paraná'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('RS', 'Rio Grande do Sul'), ('SC', 'Santa Catarina'), ('SE', 'Sergipe'), ('SP', 'São Paulo'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'estabelecimento',
                'ordering': ['store'],
                'verbose_name_plural': 'estabelecimentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('vehicle', models.CharField(max_length=50, verbose_name='veículo', unique=True)),
                ('color', models.CharField(max_length=50, verbose_name='cor')),
                ('year_of_manufacture', models.PositiveIntegerField(verbose_name='ano de fabricação')),
                ('engine_power', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='motor')),
                ('fueltype', models.CharField(choices=[('g', 'gasolina'), ('a', 'álcool'), ('d', 'diesel'), ('f', 'flex'), ('e', 'elétrico')], max_length=1, verbose_name='tipo de combustível')),
                ('transmissiontype', models.CharField(choices=[('a', 'automático'), ('m', 'manual')], max_length=1, verbose_name='tipo de câmbio')),
                ('power', models.CharField(default='-', max_length=30, verbose_name='potência')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='preço')),
                ('photo_vehicle', models.ImageField(default='vehicles/car_700x300.jpg', upload_to='vehicles')),
                ('kit_fabric', models.ForeignKey(verbose_name='kit de fábrica', to='core.Kit', related_name='vehicle_kit')),
                ('modell', models.ForeignKey(verbose_name='modelo', to='core.Modell', related_name='vehicle_model')),
            ],
            options={
                'verbose_name': 'veículo',
                'ordering': ['vehicle'],
                'verbose_name_plural': 'veículos',
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
            field=models.ForeignKey(verbose_name='estabelecimento', to='core.Store', related_name='kiosk_store'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='employee',
            name='occupation',
            field=models.ForeignKey(verbose_name='cargo', to='core.Occupation', related_name='employee_occupation'),
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
            field=models.ForeignKey(verbose_name='veículo', to='core.Vehicle', related_name='vehicle_det'),
            preserve_default=True,
        ),
    ]
