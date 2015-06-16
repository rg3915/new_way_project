# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.formats import number_format
from django.contrib.auth.models import User
# List of values for use in choices
from .lists import gender_list, treatment_list, type_address_list, uf_list, \
    type_phone_list, fueltype_list, transmissiontype_list, status_list


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(
        _('criado em'), auto_now_add=True, auto_now=False)
    modified_at = models.DateTimeField(
        _('modificado em'), auto_now_add=False, auto_now=True)

    class Meta:
        abstract = True


class Address(models.Model):
    address = models.CharField(_(u'endereço'), max_length=80)
    complement = models.CharField(
        _('complemento'), max_length=80, blank=True, null=True)
    district = models.CharField(_('bairro'), max_length=80)
    city = models.CharField(_('cidade'), max_length=80)
    uf = models.CharField(_('UF'), max_length=2, choices=uf_list)
    cep = models.CharField(_('CEP'), max_length=9)

    class Meta:
        abstract = True


class Person(TimeStampedModel, Address):
    gender = models.CharField(_(u'gênero'), max_length=1, choices=gender_list)
    first_name = models.CharField(_('nome'), max_length=100)
    last_name = models.CharField(_('sobrenome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    birthday = models.DateField(_('data de nascimento'))
    email = models.EmailField(_('email'), blank=True)
    phone = models.CharField(
        _('telefone'), max_length=15, null=True, blank=True)
    cell = models.CharField(_('celular'), max_length=15, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['first_name']

    def __str__(self):
        return self.first_name + " " + self.last_name
    full_name = property(__str__)


class Customer(Person):

    class Meta:
        verbose_name = _(u'cliente')
        verbose_name_plural = _(u'clientes')


class Employee(Person):
    user = models.OneToOneField(User)
    occupation = models.ForeignKey(
        "Occupation", verbose_name='cargo', related_name='employee_occupation')
    dealership = models.ForeignKey(
        "Dealership", verbose_name=u'concessionária', related_name='employee_dealership')
    comissioned = models.BooleanField(_('comissionado'), default=True)
    comission = models.DecimalField(
        _(u'comissão'), max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = _(u'funcionário')
        verbose_name_plural = _(u'funcionários')


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Occupation(models.Model):
    occupation = models.CharField(_('cargo'), max_length=50)

    class Meta:
        verbose_name = _('cargo')
        verbose_name_plural = _('cargos')

    def __str__(self):
        return self.occupation


class Dealership(Address):
    dealership = models.CharField(_(u'concessionária'), max_length=50)
    site = models.CharField(_('site'), max_length=100, null=True, blank=True)
    phone1 = models.CharField(
        _('telefone 1'), max_length=15, null=True, blank=True)
    phone2 = models.CharField(
        _('telefone 2'), max_length=15, null=True, blank=True)
    phone3 = models.CharField(
        _('telefone 3'), max_length=15, null=True, blank=True)

    class Meta:
        verbose_name = _(u'concessionária')
        verbose_name_plural = _(u'concessionárias')

    def __str__(self):
        return self.dealership


class DealershipDetail(models.Model):
    dealership = models.ForeignKey(
        "Dealership", verbose_name=u'concessionária', related_name='dealership_det')
    vehicle = models.ForeignKey(
        "Vehicle", verbose_name=u'veículo', related_name='vehicle_det')
    quantity_vehicle = models.PositiveIntegerField(_('quantidade'))

    def __str__(self):
        return self.dealership  # unicode(self.dealership)


class Brand(models.Model):
    brand = models.CharField(_('marca'), max_length=50, unique=True)
    photo = models.ImageField(upload_to='brands')

    class Meta:
        ordering = ['brand']
        verbose_name = u'marca'
        verbose_name_plural = u'marcas'

    def __str__(self):
        return self.brand

    def thumb(self):
        return '<img src="%s"/ width="70px">' % self.photo.url
    thumb.allow_tags = True


class Modell(models.Model):
    modell = models.CharField(_('modelo'), max_length=50, unique=True)
    brand = models.ForeignKey(
        "Brand", verbose_name=u'marca', related_name='model_brand')

    class Meta:
        ordering = ['modell']
        verbose_name = u'modelo'
        verbose_name_plural = u'modelos'

    def __str__(self):
        return self.modell


class Vehicle(models.Model):
    modell = models.ForeignKey(
        "Modell", verbose_name=u'modelo', related_name='vehicle_model')
    vehicle = models.CharField(_('veículo'), max_length=50, unique=True)
    # slug = models.SlugField(_('slug'))
    color = models.CharField(_('cor'), max_length=50)
    year_of_manufacture = models.PositiveIntegerField(_(u'ano de fabricação'))
    engine_power = models.DecimalField(
        _('motor'), max_digits=6, decimal_places=2)
    fueltype = models.CharField(
        _(u'tipo de combustível'), max_length=1, choices=fueltype_list)
    transmissiontype = models.CharField(
        _(u'tipo de câmbio'), max_length=1, choices=transmissiontype_list)
    power = models.CharField(_(u'potência'), max_length=30, default='-')
    price = models.DecimalField(_(u'preço'), max_digits=8, decimal_places=2)
    kit_fabric = models.ForeignKey(
        "Kit", verbose_name=u'kit de fábrica', related_name='vehicle_kit')
    photo_vehicle = models.ImageField(
        upload_to='vehicles', default='vehicles/car_700x300.jpg')

    class Meta:
        ordering = ['vehicle']
        verbose_name = u'veículo'
        verbose_name_plural = u'veículos'

    def __str__(self):
        return self.vehicle

    # clica no carro e retorna os detalhes dele
    def get_vehicle_url(self):
        return u"/vehicles/%i" % self.id

    def get_price(self):
        return u"R$ %s" % number_format(self.price, 2)

    def thumb(self):
        return '<img src="%s"/ width="70px">' % self.photo_vehicle.url
    thumb.allow_tags = True

    def image(self):
        return '<img src="%s"/ width="500px">' % self.photo_vehicle.url
    image.allow_tags = True


class Accessory(models.Model):
    accessory = models.CharField(_(u'accessório'), max_length=50)
    price_accessory = models.DecimalField(
        _(u'preço'), max_digits=8, decimal_places=2)
    photo_accessory = models.ImageField(
        upload_to='accessorys', blank=True, null=True)

    class Meta:
        ordering = ['accessory']
        verbose_name = u'accessório'
        verbose_name_plural = u'accessórios'

    def __str__(self):
        return self.accessory

    def get_price(self):
        return u"R$ %s" % number_format(self.price_accessory, 2)

    def thumb(self):
        return '<img src="%s"/ width="70px">' % self.photo_accessory.url
    thumb.allow_tags = True

    def image(self):
        return '<img src="%s"/ width="500px">' % self.photo_accessory.url
    image.allow_tags = True


class Kit(models.Model):
    kit = models.CharField(max_length=50)

    class Meta:
        ordering = ['kit']
        verbose_name = u'kit'
        verbose_name_plural = u'kits'

    def __str__(self):
        return self.kit


class KitDetail(models.Model):
    kit = models.ForeignKey("Kit", verbose_name='kit', related_name='kit_det')
    accessory = models.ForeignKey(
        "Accessory", verbose_name=u'accessório', related_name='accessory_kit')
    quantity_accessory = models.PositiveIntegerField(_('quantidade'))

    def __str__(self):
        return str(self.kit)


class Store(models.Model):
    store = models.CharField(_(u'estabelecimento'), max_length=65)
    phone = models.CharField(_('telefone'), max_length=15, blank=True)
    city = models.CharField(_('cidade'), max_length=80, blank=True)
    uf = models.CharField(_('UF'), max_length=2, choices=uf_list)

    class Meta:
        ordering = ['store']
        verbose_name = u'estabelecimento'
        verbose_name_plural = u'estabelecimentos'

    def __str__(self):
        return self.store


class Kiosk(models.Model):
    kiosk = models.CharField(_(u'quiosque'), max_length=50)
    store = models.ForeignKey(
        "Store", verbose_name='estabelecimento', related_name='kiosk_store')

    class Meta:
        ordering = ['kiosk']
        verbose_name = u'quiosque'
        verbose_name_plural = u'quiosques'

    def __str__(self):
        return self.kiosk


class Ordered(TimeStampedModel):
    customer = models.ForeignKey("Customer", verbose_name='cliente')
    # employee = models.ForeignKey("Employee", verbose_name=u'funcionário')
    vehicle = models.ForeignKey("Vehicle", verbose_name=u'veículo')
    kit_optional = models.ForeignKey("Kit", verbose_name='kit opcional')
    dealership = models.ManyToManyField(
        "Dealership", verbose_name=u'concessionária')
    kiosk = models.ForeignKey("Kiosk", verbose_name='quiosque')
    status = models.CharField(max_length=2, choices=status_list, default='p')

    class Meta:
        ordering = ['-id']
        verbose_name = u'pedido'
        verbose_name_plural = u'pedidos'

    def __str__(self):
        return str(self.id)

    def get_detalhe(self):
        return u"/ordered/%i" % self.id
